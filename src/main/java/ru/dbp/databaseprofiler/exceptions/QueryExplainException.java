package ru.dbp.databaseprofiler.exceptions;
/**
 * Exception for query explanation fetching failures.
 */
public class QueryExplainException extends RuntimeException {
    public QueryExplainException() {
        super("Failed to fetch query explanation");
    }

    public QueryExplainException(String message) {
        super(message);
    }
}
