duckdb-query-project/
.
├── config
│   ├── database.py
├── database
│   ├── 6a8ba9d16583414f9abce56141502022_0.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_1.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_2.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_3.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_4.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_5.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_6.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_7.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_8.parquet
│   ├── 6a8ba9d16583414f9abce56141502022_9.parquet
│   ├── database-config.md
│   ├── init-database-sql.sql
│   └── init.sql
├── docker
│   ├── docker-compose.txt
│   └── docker-setup.txt
├── docs
│   └── requirements.md
├── main.py
├── README.md
├── requirements.txt
├── setup.sh
├── src
│   ├── controllers
│   │   ├── app_controllers.py
│   │   └── vehicle_controllers.py
│   ├── database
│   │   ├── connection.py
│   │   └── queries.py
│   ├── models
│   │   ├── data_models.py
│   │   └── vehicle_data.py
│   ├── repositories
│   │   └── vehicle_repository.py
│   ├── utils
│   │   ├── exceptions.py
│   └── validations
│       └── vehicle_validations.py
└── tests
    ├── connection_test.py
    └── validation_test.py




# DuckDB Query Project

## Overview
A robust, modular Python project for executing queries against DuckDB databases.

## Features
- Structured database connection management
- Custom exception handling
- Flexible query execution
- Type-hinted code
- Easy extensibility

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Install the package: `pip install -e .`

## Usage
```python
from src.database.connection import DatabaseConnection
from src.database.queries import QueryManager

# Establish connection
db_connection = DatabaseConnection('your_database.db')
query_manager = QueryManager(db_connection)

# Execute query
result = query_manager.execute_custom_query("SELECT * FROM your_table")
print(result.data)