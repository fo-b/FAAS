# garage_door.py
from enum import Enum

class GarageDoorState(Enum):
    CLOSED = 1
    OPEN = 2
    NEITHER = 3

def split_into_axis(raw_sensor_value: str):
    values_str = raw_sensor_value.split(',')
    values_float = [float(value) for value in values_str]
    values_tuple = tuple(values_float)
    return values_tuple

def eval_garage_door_state(raw_sensor_value: str) -> GarageDoorState:
    x, y, z = split_into_axis(raw_sensor_value)
    if z < -0.8:
        return GarageDoorState.OPEN
    elif z > -0.1:
        return GarageDoorState.CLOSED
    else:
        return GarageDoorState.NEITHER
