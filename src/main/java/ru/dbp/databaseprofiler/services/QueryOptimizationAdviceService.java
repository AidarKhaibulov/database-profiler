package ru.dbp.databaseprofiler.services;


import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import ru.dbp.databaseprofiler.repositories.PgStatementRepository;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Slf4j
@Service
@RequiredArgsConstructor
public class QueryOptimizationAdviceService {

    private final PgStatementRepository pgStatementRepository;
    private final QueryExplainerService queryExplainer;

    // todo: consider moving out to global configuration
    @Value("${spring.datasource.username}")
    private String currentUser;

    public Map<String, String> analyzeQueries() {
        List<String> queries = getUserQueries(currentUser);
        return queries.stream()
                .flatMap(s -> mapQueryWithAdvice(s).entrySet().stream())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    private String generateAdviceForQuery(String s) {
        if (s.toLowerCase().startsWith("select *")) {
            //todo: move out to constant
            return "Avoid using SELECT * in SQL queries. Instead, explicitly specify the columns you need. This improves query performance, readability, and future-proofing of your code";
        } else {
            try {
                List<String> queryPlan = queryExplainer.explainQuery(s);
            }
            catch (Exception e){
                log.error("Exception while fetching query plan");
            }
            return "No advice";
        }
    }

    private Map<String, String> mapQueryWithAdvice(String s) {
        Map<String, String> map = new HashMap<>();
        map.put(s, generateAdviceForQuery(s));
        return map;
    }

    private List<String> getUserQueries(String username) {
        return pgStatementRepository.findAllUserQueries(username);
    }
}
