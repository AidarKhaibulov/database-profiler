package ru.dbp.databaseprofiler.services;

import jakarta.persistence.EntityManager;
import org.flywaydb.core.Flyway;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Testcontainers;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;


@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)@Testcontainers
class QueryExplainerServiceTest {
    @LocalServerPort
    private Integer port;

    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
            "postgres:latest"
    );
    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }



    @BeforeAll
    static void beforeAll() {
        postgres.start();
        Flyway flyway = Flyway.configure()
                .dataSource(postgres.getJdbcUrl(), postgres.getUsername(), postgres.getPassword())
                .locations("classpath:db/migration/postgres")
                .load();
        flyway.migrate();
    }

    @AfterAll
    static void afterAll() {
        postgres.stop();
    }

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