import duckdb
import os

def test_database_connection():
    """
    Test DuckDB database connection and basic operations
    """
    try:
        # Retrieve database path from environment variable
        db_path = os.getenv('DUCKDB_DATABASE_PATH', './db/vehicle_data.db')
        
        # Establish connection
        conn = duckdb.connect(db_path)
        
        # Verify table existence
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        assert "vehicle_data" in [table[0] for table in tables], "vehicle_data table not found"
        
        # Test basic query
        result = cursor.execute("SELECT COUNT(*) FROM vehicle_data").fetchone()
        print(f"Total records in vehicle_data: {result[0]}")
        
        conn.close()
        return True
    
    except Exception as e:
        print(f"Database connection test failed: {e}")
        return False

def test_parquet_loading():
    """
    Test loading Parquet files into the database
    """
    try:
        conn = duckdb.connect(':memory:')
        parquet_path = os.getenv('DUCKDB_PARQUET_PATH', './db/*.parquet')
        
        # Attempt to read Parquet files
        result = conn.execute(f"SELECT COUNT(*) FROM read_parquet('{parquet_path}')").fetchone()
        
        assert result[0] > 0, "No records found in Parquet files"
        
        conn.close()
        return True
    
    except Exception as e:
        print(f"Parquet loading test failed: {e}")
        return False

def run_database_tests():
    """
    Run all database-related tests
    """
    connection_test = test_database_connection()
    parquet_test = test_parquet_loading()
    
    return connection_test and parquet_test

if __name__ == "__main__":
    success = run_database_tests()
    exit(0 if success else 1)
