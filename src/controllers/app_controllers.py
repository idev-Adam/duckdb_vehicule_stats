from src.database.queries import QueryManager


class AppController:
    """
    Controls the application flow and user interactions.
    """
    def __init__(self, _query_manager: QueryManager):
        """
        Initializes AppController with a QueryManager instance.

        Args:
            _query_manager (QueryManager): An instance of QueryManager for handling database queries.
        """
        self._query_manager = _query_manager
