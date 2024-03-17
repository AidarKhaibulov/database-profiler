package ru.dbp.databaseprofiler.services;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.Query;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.postgresql.util.PGobject;
import org.springframework.stereotype.Service;
import ru.dbp.databaseprofiler.exceptions.QueryExplainException;
import ru.dbp.databaseprofiler.utils.StringHelper;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


@Slf4j
@Service
@RequiredArgsConstructor
public class QueryExplainerService {

    @PersistenceContext
    private EntityManager entityManager;

    @SuppressWarnings("unchecked")
    public List<String> explainQuery(String query) throws QueryExplainException{
        try {
            String queryWithParams = linkParamsToQueryIfRequired(query);
            String fullQuery = "EXPLAIN VERBOSE " + queryWithParams;
            Query explainQuery = entityManager.createNativeQuery(fullQuery);
            return explainQuery.getResultList();
        }catch (Exception e){
            throw new QueryExplainException();
        }
    }

    private String linkParamsToQueryIfRequired(String query) {
        if (!query.contains("$1"))
            return query;

        HashMap<String, HiddenValueAndTableNamePair> columnHiddenValueAndTableNameMap = new HashMap<>();
        HashMap<String, String> hiddenValueRealValueMap = new HashMap<>();

        fillColumnHiddenValueMapWithHiddenValues(query, columnHiddenValueAndTableNameMap);
        fillColumnHiddenValueAndTableNameMapWithTableNames(query, columnHiddenValueAndTableNameMap);

        fillHiddenValueRealValueMap(columnHiddenValueAndTableNameMap, hiddenValueRealValueMap);

        return createQueryWithRealValues(query, hiddenValueRealValueMap);
    }

    private String createQueryWithRealValues(String query, HashMap<String, String> hiddenValueRealValueMap) {
        StringBuilder queryWithParams = new StringBuilder(query);
        int paramIndex = 1;
        for (Map.Entry<String, String> e : hiddenValueRealValueMap.entrySet()) {
            String hiddenValue = "$" + paramIndex;
            int hiddenValueIndex = queryWithParams.indexOf(hiddenValue);
            String paramToReplace = switch (e.getValue()) {
                case "bigint", "integer" -> "1";
                case "varchar" -> "''";
                default -> throw new IllegalArgumentException("Unsupported data type");
            };
            queryWithParams.replace(hiddenValueIndex, hiddenValueIndex + hiddenValue.length(), paramToReplace);
            paramIndex++;
        }

        replaceRemainingParamsWithIntegerValues(queryWithParams);

        return queryWithParams.toString();
    }

    private void replaceRemainingParamsWithIntegerValues(StringBuilder queryWithParams) {
        Pattern pattern = Pattern.compile("\\$\\d+", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(queryWithParams);

        while (matcher.find()) {
            queryWithParams.replace(matcher.start(), matcher.end(), "1");
        }
    }

    private void fillHiddenValueRealValueMap(HashMap<String, HiddenValueAndTableNamePair> columnHiddenValueAndTableNameMap, HashMap<String, String> hiddenValueRealValueMap) {
        for (Map.Entry<String, HiddenValueAndTableNamePair> e : columnHiddenValueAndTableNameMap.entrySet()) {
            String key = e.getKey();
            String hiddenValue = e.getValue().getPair()[0];
            String tableName = e.getValue().getPair()[1];
            String columnName = StringHelper.getSubstringAfterFirstDot(key);
            String paramType = getColumnType(tableName, columnName).orElseThrow(NoSuchElementException::new);

            hiddenValueRealValueMap.put(hiddenValue, paramType);
        }
    }


    /**
     * Fills the map with table names used in the SQL query.
     *
     * @param query The SQL query in which table names need to be found
     * @param map   The map of hidden values and table names to which table names need to be added
     */
    private void fillColumnHiddenValueAndTableNameMapWithTableNames(String query, HashMap<String, HiddenValueAndTableNamePair> map) {
        for (Map.Entry<String, HiddenValueAndTableNamePair> e : map.entrySet()) {
            Pattern pattern = Pattern.compile("\\bFROM\\s+(\\w+)\\s+(" + StringHelper.getSubstringBeforeFirstDot(e.getKey()) + ")\\b", Pattern.CASE_INSENSITIVE);
            Matcher matcher = pattern.matcher(query);

            if (matcher.find()) {
                String tableName = matcher.group(1);
                HiddenValueAndTableNamePair value = e.getValue();
                value.getPair()[1] = tableName;
                e.setValue(value);
            }
        }
    }

    private void fillColumnHiddenValueMapWithHiddenValues(String query, HashMap<String, HiddenValueAndTableNamePair> map) {
        Pattern pattern = Pattern.compile("\\b(\\w+\\.\\w+)=(\\$\\d+)\\b");
        Matcher matcher = pattern.matcher(query);

        while (matcher.find()) {
            String key = matcher.group(1);
            HiddenValueAndTableNamePair value = new HiddenValueAndTableNamePair();
            value.getPair()[0] = matcher.group(2);
            map.put(key, value);
        }
    }

    private Optional<String> getColumnType(String tableName, String columnName) {
        String sqlQuery = "SELECT pg_typeof(" + columnName + ") AS data_type FROM " + tableName + " LIMIT 1";
        Query query = entityManager.createNativeQuery(sqlQuery);
        Object result = query.getSingleResult();
        if (result instanceof PGobject pgObject) {
            return Optional.ofNullable(pgObject.getValue());
        }

        return Optional.empty();
    }

    @Getter
    @Setter
    static class HiddenValueAndTableNamePair {
        private String[] pair;

        public HiddenValueAndTableNamePair() {
            this.pair = new String[2];
        }
    }
}
