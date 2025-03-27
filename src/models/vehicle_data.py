
"""
This module defines vehicle types using an enumeration and provides default distance ranges and intervals.
"""
from typing import List, Tuple
from enum import Enum

class VehicleType(Enum):
    """
    Enumeration of different vehicle types.
    Used to classify vehicles in data processing and analysis.
    """
    CAR = "car"
    IGNORE = "ignore"
    TRAILER = "trailer"
    TRUCK = "truck"
    BICYCLE = "bicycle"
    VAN = "van"
    BUS = "bus"
    SCOOTER = "scooter"
    BIKE = "bike"
    PICKUP = "pickup"
    TRIKE = "trike"

# Default range for distance calculations
distance_range_default:Tuple = (0, 100)

# Default intervals for categorizing distances
distance_intervals_default =[
        (1, 10), (11, 20), (21, 30), (31, 40), 
        (41, 50), (51, 60), (61, 70), (71, 80), 
        (81, 90), (91, 100)
    ]
