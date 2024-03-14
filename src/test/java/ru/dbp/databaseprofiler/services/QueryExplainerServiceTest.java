package ru.dbp.databaseprofiler.services;

import jakarta.persistence.EntityManager;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import ru.dbp.databaseprofiler.BasePostgresContainerTest;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;


@ActiveProfiles("test")
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class QueryExplainerServiceTest extends BasePostgresContainerTest {

    @Autowired
    private EntityManager entityManager;

    @Autowired
    private QueryExplainerService queryExplainer;

    @Test
    @DisplayName("Test explanation of query with one param")
    void test01() {
        String expectedExplanation = "Seq Scan on public.songs s1_0";
        String query = """
                SELECT s1_0.id, s1_0.band_id, s1_0.duration_in_seconds, s1_0.lyrics, s1_0.title
                FROM songs s1_0\s
                WHERE s1_0.duration_in_seconds=$1
                """;

        List<String> queryPlan = queryExplainer.explainQuery(query);

        Optional<String> hasExpectedExplanation = queryPlan.stream().filter(x -> x.contains(expectedExplanation)).findAny();
        assertThat(hasExpectedExplanation).isPresent();
    }

    @Test
    @DisplayName("Test explanation of query with two params")
    void test02() {
        String expectedExplanation = "Seq Scan on public.songs s1_0";
        String query = "SELECT * FROM songs s1_0 WHERE  s1_0.duration_in_seconds=$1 and s1_0.band_id=$2";

        List<String> queryPlan = queryExplainer.explainQuery(query);

        Optional<String> hasExpectedExplanation = queryPlan.stream().filter(x -> x.contains(expectedExplanation)).findAny();
        assertThat(hasExpectedExplanation).isPresent();
    }

    @Test
    @DisplayName("Test explanation of query with two params and one LIMIT param")
    void test03() {
        String expectedExplanation = "Seq Scan on public.songs s1_0";
        String query = "SELECT * FROM songs s1_0 WHERE  s1_0.duration_in_seconds=$1 and s1_0.band_id=$2 LIMIT $3";

        List<String> queryPlan = queryExplainer.explainQuery(query);

        Optional<String> hasExpectedExplanation = queryPlan.stream().filter(x -> x.contains(expectedExplanation)).findAny();
        assertThat(hasExpectedExplanation).isPresent();
    }

}