package ru.dbp.databaseprofiler;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class DatabaseProfilerApplication {

	public static void main(String[] args) {
		SpringApplication.run(DatabaseProfilerApplication.class, args);
	}


}

