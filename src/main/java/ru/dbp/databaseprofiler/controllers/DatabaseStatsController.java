package ru.dbp.databaseprofiler.controllers;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import ru.dbp.databaseprofiler.models.PgStatement;
import ru.dbp.databaseprofiler.services.PostgreSQLPgStatementsService;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class DatabaseStatsController {
    private final PostgreSQLPgStatementsService pgStatementsProcessorService;

    @GetMapping("/getTopNSlowestQueries/{n}")
    public ResponseEntity<List<PgStatement>> getTopNSlowestQueries(@PathVariable int n) {
        return ResponseEntity.ok(pgStatementsProcessorService.getTopNSlowestQueries(n));
    }

}
