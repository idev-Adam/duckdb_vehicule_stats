class DatabaseConnectionError(Exception):
    """Raised when database connection fails."""
    pass

class QueryExecutionError(Exception):
    """Raised when query execution encounters an error."""
    pass