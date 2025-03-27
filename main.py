"""
Vehicle Detection Statistics Analysis Script

This script demonstrates how to retrieve and analyze vehicle detection statistics
from a database using the VehicleControllers class.

Dependencies:
- pandas
- Custom modules: config.database, src.controllers.vehicle_controllers, 
                  src.database.connection, src.database.queries

Prerequisites:
1. Ensure the database filepath is correctly configured in config.database
2. Verify that the database connection and query manager are properly set up
3. Make sure vehicle detection data is available in the database

Usage Examples:
    # Example 1: Get vehicle stats for full distance range
    vehicle_stats_df = vehicle_controller.get_vehicle_detection_stats({
        "distance_range": (0, 100),
        "distance_intervals": [
            (1, 10), (11, 20), (21, 30), (31, 40), 
            (41, 50), (51, 60), (61, 70), (71, 80), 
            (81, 90), (91, 100)
        ]
    })

    # Example 2: Get vehicle stats for specific vehicle type and distance range
    vehicle_stats_df = vehicle_controller.get_vehicle_detection_stats({
        "distance_range": (20, 80),
        "distance_intervals": [
            (1, 10), (11, 20), (21, 30), (31, 40), 
            (41, 50), (61, 70), (71, 80), 
            (81, 90), (91, 100)
        ],
        "vehicle_type": "car"
    })

Note:
- The script supports filtering by distance range and vehicle type
- Metadata provides additional context about the statistics
"""


from config.database import database_filepath
from src.controllers.vehicle_controllers import VehicleControllers
from src.database.connection import DatabaseConnection
from src.database.queries import QueryManager
from src.models.data_models import QueryResult



def main():
    """
    Main function to demonstrate vehicle detection statistics retrieval.
    
    This function:
    1. Establishes a database connection
    2. Creates a query manager
    3. Initializes the vehicle controllers
    4. Retrieves vehicle detection statistics for different scenarios
    5. Prints the results
    """

    try:
        # Establish database connection and create query manager
        db_connection = DatabaseConnection(database_path=database_filepath)
        query_manager = QueryManager(db_connection=db_connection)


        # Initialize vehicle controllers
        vehicle_controller = VehicleControllers(query_manager=query_manager)
        
        # Scenario 1: get all results
        vehicle_stats:QueryResult = vehicle_controller.get_vehicle_detection_stats(requests={})

        # Print full range statistics
        print("\nData:")
        print(vehicle_stats.data.to_string(index=False))
        print("\nMetadata:")
        print(vehicle_stats.metadata)


        # Scenario 2: Car-specific statistics with limited distance range
        vehicle_stats_car:QueryResult = vehicle_controller.get_vehicle_detection_stats(requests={
            "distance_range": (20, 80),
            "distance_intervals": [
                (1, 10), (11, 20), (21, 30), (31, 40), 
                (41, 50),  (61, 70), (71, 80), 
                (81, 90), (91, 100)
            ],
            "vehicle_type": "car"  # Valid Enum Value$
        })

        # Print car-specific statistics
        print("\nData:")
        print(vehicle_stats_car.data.to_string(index=False))
        print("\nMetadata:")
        print(vehicle_stats_car.metadata)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()