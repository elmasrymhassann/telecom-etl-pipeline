# # Telecom ETL Pipeline

## Project Overview
End-to-end Telecom ETL Pipeline using:

- Python
- Pandas
- PostgreSQL
- Docker
- Apache Airflow
- Power BI

## Architecture

CSV Data
↓
Python ETL
↓
PostgreSQL
↓
Airflow Orchestration
↓
Power BI Dashboard

## Technologies Used

- Python
- SQLAlchemy
- PostgreSQL
- Docker
- Apache Airflow
- Power BI
- Pandas
- Matplotlib

## Features

- Automated ETL pipeline
- Dockerized infrastructure
- Airflow DAG scheduling
- PostgreSQL data warehouse
- Power BI dashboard
- Daily automated workflow

## How To Run

### Start Docker Containers

```bash
docker compose up -d
```

### Run ETL Pipeline

```bash
python src/database.py
```

### Open Airflow

```text
http://localhost:8080
```

## Future Improvements

- Kafka Streaming
- Azure Deployment
- CI/CD Pipeline
- Real-time Analytics