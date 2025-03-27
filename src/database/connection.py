import typing as t
import duckdb
import pandas as pd
from src.utils.exceptions import QueryExecutionError, DatabaseConnectionError

class DatabaseConnection:
    """
    Manages database connection and provides core database interaction methods.
    
    Attributes:
        _connection: DuckDB database connection
    """
    
    def __init__(self, database_path: str):
        """
        Initialize database connection.
        
        Args:
            database_path: Path to the DuckDB database file
        
        Raises:
            DatabaseConnectionError: If connection cannot be established
        """
        try:
            self._connection = duckdb.connect(database_path,read_only=True)
        except Exception as e:
            raise DatabaseConnectionError(f"Failed to connect to database: {e}")
    
    def execute_query(self, query: str, params: t.Optional[t.List[t.Any]] = None) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a pandas DataFrame.
        
        Args:
            query: SQL query to execute
            params: Optional query parameters
        
        Returns:
            pandas.DataFrame containing query results
        
        Raises:
            QueryExecutionError: If query execution fails
        """
        try:
            return self._connection.execute(query, params).df()
        except Exception as e:
            raise QueryExecutionError(f"Query execution failed: {e}")
    
    def close(self):
        """Close the database connection."""
        self._connection.close()
