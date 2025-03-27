from src.database.connection import DatabaseConnection
from src.models.data_models import QueryResult
from src.utils.exceptions import QueryExecutionError
import typing as t
class QueryManager:
    """
    Manages database queries with additional abstraction and error handling.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initializes QueryManager with a database connection.

        Args:
            db_connection (DatabaseConnection): An active database connection instance.
        """
        self._db_connection = db_connection
    
    def execute_custom_query(self, query: str, params: t.Optional[t.List[t.Any]] = None) -> QueryResult:
        """
        Executes a custom SQL query with optional parameters.

        Args:
            query (str): The SQL query to be executed.
            params (Optional[List[Any]]): A list of optional query parameters.

        Returns:
            QueryResult: An object containing query results and metadata (e.g., row count, column names).

        Raises:
            QueryExecutionError: If the query execution fails.
        """
        try:
            result_df = self._db_connection.execute_query(query, params)
            return QueryResult(
                data=result_df,
                metadata={
                    'row_count': len(result_df),
                    'columns': list(result_df.columns)
                }
            )
        except Exception as e:
            raise QueryExecutionError(f"Custom query failed: {e}")
        