package ru.dbp.databaseprofiler.utils;

import jdk.jfr.Enabled;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;

@Slf4j
@Component
public class LogReader {
    @Value("${log.directory}")
    private String logDirectory;

    @Scheduled(fixedRateString = "${log.reader.interval}")
    public void readLogs() {
        File directory = new File(logDirectory);
        File[] files = directory.listFiles();

        if (files != null) {
            for (File file : files) {
                if (file.isFile() && file.getName().endsWith(".csv")) {
                    String csvFilePath = file.getAbsolutePath();
                    String fileData;

                    try {
                        fileData = new String(Files.readAllBytes(Paths.get(csvFilePath)));
                        log.debug("File {} has been read", csvFilePath);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}


