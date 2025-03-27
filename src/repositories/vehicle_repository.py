from src.database.queries import QueryManager
from src.validations.vehicle_validations import VehicleValidation
import pandas as pd
from src.models.data_models import QueryResult



class VehicleDataRepository:
    """
    Repository for handling vehicle-related database queries.
    """
    def __init__(self, query_manager: QueryManager):
        """
        Initialize repository with database controller.
        
        Args:
            query_manager: Established database connection controller
        """
        self._db_controller = query_manager

    def format_distance_columns(self, params: VehicleValidation) -> str:
        """
        Generate SQL query fragments for distance interval columns.
        
        Each column represents a percentage of detections within a specified distance range.
        
        Args:
            params: VehicleValidation object containing distance range and intervals.
        
        Returns:
            A formatted string representing SQL column calculations for distance intervals.
        """
        return ", ".join([
            f"ROUND(100.0 * SUM(CASE WHEN distance BETWEEN {start} AND {end} THEN detection::INTEGER END) / NULLIF(COUNT(CASE WHEN distance BETWEEN {start} AND {end} THEN 1 END), 0), 2) AS \"{start}-{end}\""
            for start, end in params.distance_intervals if start >= params.distance_range[0] and end <= params.distance_range[1]
        ])

    def detection_statistics(self, params: VehicleValidation) -> QueryResult:
        """
        Retrieve comprehensive vehicle detection statistics based on provided parameters.
        
        Args:
            params: VehicleValidation object containing filters like vehicle type and distance range.
        
        Returns:
            A QueryResult containing detection statistics for various distance intervals as Panda dataframe and dict metadata.
        """
        base_query = """
        SELECT
            vehicle_type,
            {distance_columns}
        FROM vehicle_data
        {where_clause}
        GROUP BY vehicle_type
        """


        distance_columns:str = self.format_distance_columns(params)

        
        # Construct dynamic WHERE clause based on provided filters
        conditions = []
        query_params = []

        if params.vehicle_type:
            conditions.append("vehicle_type = ?")
            query_params.append(params.vehicle_type.value)
        
        if params.distance_range:
            conditions.append("distance BETWEEN ? AND ?")
            query_params.extend(params.distance_range)

        # Combine conditions into a WHERE clause, if any exist
        where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

        # Format the final SQL query with dynamic values
        formatted_query = base_query.format(
            distance_columns=distance_columns,
            where_clause=where_clause
        )

        # Execute the query and return the result as QueryResult
        return self._db_controller.execute_custom_query(formatted_query, query_params)