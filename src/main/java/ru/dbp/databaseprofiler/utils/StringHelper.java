package ru.dbp.databaseprofiler.utils;

import lombok.experimental.UtilityClass;

/**
 * Provides additional string methods
 */
@UtilityClass
public class StringHelper {
    /**
     * Extracts the substring before the first occurrence of a dot ('.') in the input string.
     *
     * @param input the input string
     * @return the substring before the first dot; if no dot is found, returns the input string
     */
    public String getSubstringAfterFirstDot(String input) {
        int dotIndex = input.indexOf('.');
        if (dotIndex != -1) {
            return input.substring(dotIndex + 1);
        } else {
            return input;
        }
    }

    /**
     * Extracts the substring after the first occurrence of a dot ('.') in the input string.
     *
     * @param input the input string
     * @return the substring after the first dot; if no dot is found, returns the input string
     */
    public String getSubstringBeforeFirstDot(String input) {
        int dotIndex = input.indexOf('.');
        if (dotIndex != -1) {
            return input.substring(0, dotIndex);
        } else {
            return input;
        }
    }
}
