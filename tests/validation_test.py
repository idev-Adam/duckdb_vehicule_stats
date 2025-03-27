import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.validations.vehicle_validations import VehicleValidation

def test_default():
    """
    Test default case for VehicleValidation
    Ensures valid data passes without errors.
    """
    data = {
        "distance_range": (0, 100),
        "distance_intervals": [
            (1, 10), (11, 20), (21, 30), (31, 40), 
            (41, 50), (51, 60), (61, 70), (71, 80), 
            (81, 90), (91, 100)
        ],
        "vehicle_type": "car"  # Valid Enum Value
    }
    try:
        # Validate the data
        VehicleValidation(**data)
        return True
    
    except Exception as e:
        print(f"default validation failed: {e}")
        return False



def test_bad_range():
    """
    Test VehicleValidation with an invalid distance range.
    Expected: Validation should fail because the range has a negative value.
    """
    data = {
        "distance_range": (-100, 100),  # Invalid range (negative value)
        "distance_intervals": [
            (1, 10), (11, 20), (21, 30), (31, 40), 
            (41, 50), (51, 60), (61, 70), (71, 80), 
            (81, 90), (91, 100)
        ],
        "vehicle_type": "car"  # Valid Enum Value
    }
    try:
        # Validate the data, expected to raise an exception
        VehicleValidation(**data)
        print(f"bad range validation failed: {e}")
        return False
    
    except Exception as e:
        return True
    


def test_invalid_vehicle_type():
    """
    Test VehicleValidation with an invalid vehicle type.
    Expected: Validation should fail because "ski" is not a valid vehicle type.
    """
    data = {
        "distance_range": (30, 100),
        "distance_intervals": [
            (1, 10), (11, 20), (21, 30), (31, 40), 
            (41, 50), (51, 60), (61, 70), (71, 80), 
            (81, 90), (91, 100)
        ],
        "vehicle_type": "ski"  
    }
    try:
        # Validate the data, expected to raise an exception
        VehicleValidation(**data)
        print(f"bad vehicle type failed: {e}")
        return False
    
    except Exception as e:
        return True
    

def run_all_tests():
    """
    Run all validation tests and yield their results.
    """
    yield test_default()
    yield test_bad_range()
    yield test_invalid_vehicle_type()

if __name__ == "__main__":
    success = all(run_all_tests())
    exit(0 if success else 1)
