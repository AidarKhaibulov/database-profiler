package ru.dbp.databaseprofiler.controllers;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.dbp.databaseprofiler.services.QueryOptimizationAdviceService;

import java.util.Map;

@RestController
@RequiredArgsConstructor
public class PerformanceOptimizationController {

    private final QueryOptimizationAdviceService adviceService;

    @PostMapping("/analyze-queries")
    public ResponseEntity<Map<String,String>> analyzeQueries() {
        Map<String,String> result = adviceService.analyzeQueries();

        return ResponseEntity.ok(result);
    }

}
