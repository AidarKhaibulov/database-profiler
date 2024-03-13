package ru.dbp.databaseprofiler.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Entity(name = "pg_stat_statements")
@Getter
@Setter
public class PgStatement {
    @Id
    private String queryid;
    private String query;
    private Long totalExecTime;
    private Long userid;
}
