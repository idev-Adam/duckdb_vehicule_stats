from pydantic import BaseModel, conint, validator, Field
from typing import List, Tuple
from src.models.vehicle_data import VehicleType, distance_range_default, distance_intervals_default

# Pydantic model for vehicle data validation
class VehicleValidation(BaseModel):
    # Tuple representing a valid range of distances (non-negative integers)
    distance_range: Tuple[conint(ge=0), conint(ge=0)] = Field(default_factory=lambda: distance_range_default)  # Non-negative integers

    # List of tuples representing valid distance intervals (each with non-negative values)
    distance_intervals: List[Tuple[conint(ge=0), conint(ge=0)]] = Field(default_factory=lambda:distance_intervals_default)

    # Vehicle type must be a valid VehicleType enum (imported from vehicle_data)
    vehicle_type: VehicleType = None

    @validator("distance_range")
    def check_distance_range(cls, v):
        """Ensure that the start of the range is less than or equal to the end."""
        if v[0] > v[1]:
            raise ValueError("Invalid range: start must be ≤ end")
        return v

    @validator("distance_intervals")
    def check_intervals(cls, v):
        """Ensure each interval is valid (min must be strictly less than max)."""

        for min_val, max_val in v:
            if min_val >= max_val:
                raise ValueError(f"Invalid interval: ({min_val}, {max_val}) - min must be < max")
        return v

# Example Usage
