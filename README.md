# Transportation Analytics | Databricks Data Engineering Project

This project builds a data pipeline using **Databricks, PySpark, SQL, and Amazon S3** to process transportation trip data and prepare it for reporting and analysis.

The pipeline takes raw data, cleans and transforms it, and creates final datasets that can be used in dashboards.

## Project Architecture

![Transportation Data Pipeline](docs/architecture.png)

### How It Works

1. **Source Data:** Trip and city data are stored as CSV files in Amazon S3.
2. **Bronze Layer:** Raw data is loaded into Databricks.
3. **Silver Layer:** Data is cleaned, transformed, and validated.
4. **Gold Layer:** Final datasets and city-specific SQL views are created for analysis.
5. **Analytics:** The final data can be used in dashboards and reports.

The project follows the **Medallion Architecture: Bronze → Silver → Gold**.

## Technologies Used

- **Databricks:** Runs the data pipeline.
- **PySpark:** Processes and transforms data.
- **SQL:** Creates analytical datasets and views.
- **Amazon S3:** Stores the source CSV files.
- **Auto Loader:** Supports incremental file ingestion.
- **Delta Lake:** Stores processed data reliably.
- **Spark Declarative Pipelines (SDP):** Defines and manages pipeline transformations.

## Project Structure

```text
transportation-databricks-sdp/
│
├── README.md
├── .gitignore
│
├── docs/
│   ├── architecture.png
│   └── data_pipeline.png
│
├── src/
│   ├── bronze/
│   │   ├── city_bronze.py
│   │   └── trips_bronze.py
│   │
│   ├── silver/
│   │   ├── city_silver.py
│   │   ├── trips_silver.py
│   │   └── calender_silver.py
│   │
│   └── gold/
│       ├── fact_trips.sql
│       └── city-specific SQL files
│
├── config/
│   └── pipeline-configuration.example.json
│
├── data/
│   └── README.md
│
└── screenshots/
    └── README.md
```

## Data Pipeline Layers

### 1. Bronze — Raw Data

- Loads city and trip data from Amazon S3.
- Uses Databricks Auto Loader for trip data ingestion.
- Adds metadata such as source file path and ingestion time.

### 2. Silver — Clean Data

- Cleans and standardizes the source data.
- Converts columns into appropriate data types.
- Applies data-quality checks.
- Creates a calendar dataset for date-based analysis.
- Configures CDC processing for trip records.

### 3. Gold — Analytics-Ready Data

- Combines trip, city, and calendar data where defined by the SQL transformations.
- Creates a central `fact_trips` dataset.
- Provides city-specific SQL views for cities such as Surat, Jaipur, Kochi, and Indore.
- Prepares data for dashboards and business reporting.

## Pipeline Lineage

![Databricks Pipeline Lineage](docs/data_pipeline.png)

This image shows how data moves between source tables, transformations, the main `fact_trips` dataset, and city-specific outputs.

## Source Data

The project uses two Amazon S3 locations:

**City data**
```text
s3://cb-good-cab-002/data-source/city
```

**Trip data**
```text
s3://cb-good-cab-002/data-source/trips
```

The source CSV files are not included in this repository. You need access to these locations or must replace them with your own data paths.

## How to Run

1. Open your Databricks workspace.
2. Ensure that the source CSV files are accessible.
3. Import the Python files from the `src/` folder.
4. Configure the pipeline source paths and target catalog.
5. Set the required calendar start and end dates.
6. Run the Bronze and Silver transformations.
7. Execute the Gold SQL definitions after the upstream tables are ready.
8. Verify the output tables and query results.

## Validation Checklist

- [ ] Bronze tables created successfully.
- [ ] Silver transformations completed successfully.
- [ ] Calendar dataset generated.
- [ ] CDC processing validated.
- [ ] Gold `fact_trips` dataset created.
- [ ] City-specific SQL views checked.
- [ ] Pipeline execution screenshots added.

## Key Learnings

- Building a data pipeline with Databricks.
- Working with PySpark and SQL.
- Implementing Bronze, Silver, and Gold layers.
- Ingesting files from Amazon S3.
- Applying data-quality checks.
- Understanding CDC and incremental ingestion.
- Preparing data for analytics and dashboards.

## Project Summary

This project demonstrates how raw transportation data can be transformed into clean, structured, and analytics-ready datasets using modern Data Engineering tools.

**Architecture:** Bronze → Silver → Gold

**Languages:** Python, PySpark, SQL

**Platform:** Databricks

**Source Storage:** Amazon S3
