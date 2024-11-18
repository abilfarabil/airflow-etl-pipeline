# ETL Pipeline Project

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to extract data from two different sources: `sales_data.csv` and `customers_data.json`. The project demonstrates practical understanding of using Airflow for managing ETL workflows and storing results in a SQLite database.

## Prerequisites
- Docker and Docker Compose
- Python 3.8+
- SQLite
- DBeaver (for SQLite database management)

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/abilfarabil/airflow-etl-pipeline.git
   ```

2. Navigate to project directory:
   ```bash
   cd [project-directory]
   ```

3. Start Airflow using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Features
- ETL pipeline implementation using Apache Airflow
- Data extraction from CSV and JSON sources
- Data transformation and cleaning
- Loading data into SQLite database
- Parameterized DAG execution
- Automated workflow management

## Documentation

### DAG Configuration
The DAG can be triggered with different configurations based on the source type:

1. For CSV files:
```json
{
    "source_type": "csv"
}
```

2. For JSON files:
```json
{
    "source_type": "json"
}
```

### Implementation Steps and Results

1. DAG Configuration
![DAG Configuration](images/1_Screenshot_Pengaturan_DAG.png)
- Shows all configurations related to the DAG, including DAG name and other parameters.

2. CSV Configuration Parameters
![CSV Configuration Parameters](images/2_Screenshot_Parameter_Konfigurasi_untuk_CSV.png)
- Displays parameter settings for `sales_data.csv` extraction.

3. CSV DAG Run Status
![CSV DAG Run](images/3_Screenshot_DAG_Run_untuk_CSV.png)
- DAG run status when processing CSV file.

4. CSV DAG Graph
![CSV DAG Graph](images/4_Screenshot_Graf_DAG_untuk_CSV.png)
- Workflow visualization for CSV file processing.

5. SQLite Results After CSV Processing
![SQLite Results Post-CSV](images/5_Screenshot_Hasil_di_SQLite_Setelah_CSV.png)
- Extracted data from `sales_data.csv` in SQLite database.

6. JSON Configuration Parameters
![JSON Configuration Parameters](images/6_Screenshot_Parameter_Konfigurasi_untuk_JSON.png)
- Displays parameter settings for `customers_data.json` extraction.

7. JSON DAG Run Status
![JSON DAG Run](images/7_Screenshot_DAG_Run_untuk_JSON.png)
- DAG run status when processing JSON file.

8. JSON DAG Graph
![JSON DAG Graph](images/8_Screenshot_Graf_DAG_untuk_JSON.png)
- Workflow visualization for JSON file processing.

9. SQLite Results After JSON Processing
![SQLite Results Post-JSON](images/9_Screenshot_Hasil_di_SQLite_Setelah_JSON.png)
- Extracted data from `customers_data.json` in SQLite database.

## Technologies Used
- Python 3.8+
- Apache Airflow 2.x
- SQLite 3
- Docker & Docker Compose
- DBeaver (latest version)

## References
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Docker Documentation](https://docs.docker.com/)

## Conclusion
This project demonstrates how Airflow can be utilized to automate ETL processes from various data sources. Through DAG configuration and parameterization, you can easily extract, transform, and load data into databases, which is an essential skill in data engineering development.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.
8. Mempertahankan semua screenshot dengan deskripsi yang lebih terstruktur

Semua gambar tetap dipertahankan dengan nama file yang sama, hanya deskripsinya yang diubah ke dalam Bahasa Inggris untuk konsistensi.
