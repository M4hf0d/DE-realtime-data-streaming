# End-to-End Data Engineering Pipeline

End-to-end data pipeline from data ingestion to processing and storage, using Apache Airflow, Python, Apache Kafka, Zookeeper, Apache Spark, and Cassandra. The setup is containerized with Docker.
Automating data ingestion, processing, and storage, enhancing efficiency and scalability. It provides real-time insights with minimal manual intervention

 
![Pipeline Diagram](https://github.com/M4hf0d/DE-realtime-data-streaming/blob/master/diag.gif)

## Components

- **Data Source**: Fetches random user data from randomuser.me API.
- **Apache Airflow**: Orchestrates the pipeline and stores data in PostgreSQL.
- **Apache Kafka and Zookeeper**: Streams data from PostgreSQL to Spark.
- **Control Center and Schema Registry**: Manages Kafka stream monitoring and schema.
- **Apache Spark**: Processes the data using master and worker nodes.
- **Cassandra**: Stores the processed data.


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


