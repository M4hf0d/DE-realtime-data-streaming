# End-to-End Data Engineering Pipeline

## Introduction
End-to-end data pipeline from data ingestion to processing and storage, using Apache Airflow, Python, Apache Kafka, Zookeeper, Apache Spark, and Cassandra. The setup is containerized with Docker.
 This pipeline architecture is designed to handle real-time data processing, providing businesses with up-to-date insights and analytics. By leveraging scalable and distributed technologies, the solution supports large volumes of data, ensuring robust data flow, quick processing, and reliable storage, which are critical for data-driven decision-making.
## Components

- **Data Source**: Fetches random user data from randomuser.me API.
- **Apache Airflow**: Orchestrates the pipeline and stores data in PostgreSQL.
- **Apache Kafka and Zookeeper**: Streams data from PostgreSQL to Spark.
- **Control Center and Schema Registry**: Manages Kafka stream monitoring and schema.
- **Apache Spark**: Processes the data using master and worker nodes.
- **Cassandra**: Stores the processed data.

## What I Learned
- Pipeline orchestration and task scheduling.
- Real-time data streaming with Kafka.
- Distributed processing with Spark.
- Containerization for consistent deployment.

## Technologies

### Apache Airflow
- Manages workflow orchestration and task scheduling.
-  Simplifies complex workflows with dependency management.

### Apache Kafka
- Streams data between components.
- Handles high-throughput, real-time data streaming.

### Apache Zookeeper
- Manages Kafka brokers.
- Ensures distributed coordination and configuration management.

### Apache Spark
- Processes data in parallel.
- Fast data processing across multiple nodes.

### PostgreSQL
- Stores initial ingested data.


