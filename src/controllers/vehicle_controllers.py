from .app_controllers import AppController
import pandas as pd
from src.validations.vehicle_validations import VehicleValidation
from src.repositories.vehicle_repository import VehicleDataRepository
from src.models.data_models import QueryResult

class VehicleControllers(AppController):
    """
    Controller class for handling vehicle-related operations.

    This class interacts with the VehicleDataRepository to retrieve vehicle detection statistics
    based on validated request parameters.
    """
    def __init__(self, query_manager):
        """
        Initialize the VehicleControllers with a query manager.

        Args:
            query_manager: The query manager instance used for database interactions.
        """
        super().__init__(query_manager)
        self._repository:VehicleDataRepository = VehicleDataRepository(self._query_manager)


    def get_vehicle_detection_stats(self, requests:dict) -> QueryResult:
        """
        Retrieve vehicle detection statistics based on request parameters.

        Args:
            requests (dict): A dictionary containing request parameters.

        Returns:
            QueryResult: 
                data: A DataFrame containing vehicle detection statistics.
                metadata: A dictionary containing metadata like row count and column names.
        """

        data_validated:VehicleValidation  = VehicleValidation(**requests)

        vehicule_stats_data =  self._repository.detection_statistics(
            params = data_validated
        )

        return vehicule_stats_data