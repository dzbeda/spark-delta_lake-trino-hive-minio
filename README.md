# Spark, Delta Lake, Trino, Hive, and MinIO Project

This repository contains all the project files needed to set up and run a scalable big data solution using Spark, Delta Lake, Trino, Hive, and MinIO. The setup includes Docker Compose files, configuration files for Trino and Hive, as well as scripts to help you deploy and manage the services efficiently.

## Project Overview

In this project, you'll find everything required to:
- Generate data using Apache Spark in Delta Lake format (both partitioned and non-partitioned)
- Store data on MinIO’s S3-compatible storage
- Query the data using Trino and Hive, leveraging a scalable SQL engine solution for big data management

## Key Components
- **Apache Spark**: Used to generate and manage data in Delta Lake format
- **Delta Lake**: Ensures reliable and consistent data storage with ACID transactions
- **MinIO**: S3-compatible storage solution used to store the Delta Lake data
- **Trino (formerly Presto)**: Distributed SQL query engine used to query the data
- **Hive Metastore**: Provides the metadata repository required for querying data through Trino

## Medium Blog Series

1. Streamlining Big Data with Spark: Writing and Reading Delta Lake Format on MinIO-S3 Storage - https://medium.com/@dudu.zbeda_13698/streamlining-big-data-with-spark-writing-and-reading-delta-lake-format-on-minio-1700060eaa72

2. Setting Up Trino with Hive to Query Delta Lake Data on MinIO: A Scalable Big Data Solution
https://medium.com/@dudu.zbeda_13698/setting-up-trino-with-hive-to-query-delta-lake-data-on-minio-a-scalable-big-data-solution-a7e2392e04f4

## Repository files

In this project, you'll find everything required to:
- write-delta-to-minio.py - using this script you can generate none-partitioned data-lake records on MINIO-S3
- write-delta-partitioned-to-minio.py - using this script you can generate partitioned data-lake records on MINIO-S3
- read-delta-from-minio.py - using this script you can read partitioned and none-partitioned data-lake records from MINIO-S3
- docker-compose folder - In this folder, you will find the `docker-compose` file that is required to run Trino, Hive, and Postgres. The folder includes all necessary configurations files to get the services running smoothly. 
- Kubernetes folder - In this folder, you will find all Kubernetes manifests that are required to run the solution on the Kubernetes cluster 


## Connect on LinkedIn and on Medium
Feel free to connect with me on LinkedIn or Medium for more insights on Big Data, DevOps, and cloud-native solutions:
www.linkedin.com/in/davidzbeda

https://medium.com/@dudu.zbeda_13698

***David Zbeda***

