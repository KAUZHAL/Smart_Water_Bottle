from math import pi
from datetime import datetime

def distance_to_volume(distance: float, bottle_height = 16.5, bottle_radius = 4.25):
    return int(pi * (bottle_radius **2 ) * (distance))


def log_raw_data(distance: int, timestamps: list, distances: list):
    timestamps.append(datetime.now())
    distances.append(distance)

def amount_drunk(distance: int, distances: list, water_drunk: list, timestamps: list):
    try:
        current_distance = distance - distances[-1] 
    except IndexError:
        current_distance = distance

    if current_distance > 0:
        timestamps.append(datetime.now())
        water_drunk.append(distance_to_volume(current_distance))


from random import randint
def dummy_sensor():
    yield randint(0, 16)

