from math import pi
import matplotlib.pyplot as plt
from datetime import datetime
from time import sleep

def distance_to_volume(distance, bottle_height = 16.5, bottle_radius = 4.25):
    return pi * (bottle_radius **2 ) * (bottle_height - distance)

def log_raw_data(distance: int, timestamps: list, distances: list):
    timestamps.append(datetime.now())
    distances.append(distance)


def amount_drunk(distance: int, distances: list, water_drunk: list):
    current_distance = distance - distances[-1]
    # print(f"current_distance: {current_distance}")
    water_drunk.append(current_distance)


from random import randint
def dummy_sensor():
    yield randint(0, 16)

