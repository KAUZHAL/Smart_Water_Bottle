from user_data import log_raw_data, dummy_sensor, amount_drunk
from time import sleep

bottle_radius = 4.25 # In cm
bottle_height = 16.5 # In cm

bottle_volume = 936.5

if __name__ == "__main__":

    distances = [0] # Bottle is full.
    distance_timestamps = []

    water_timestamps = []
    water_drunk = [0]

    while True:
        distance = next(dummy_sensor())
        amount_drunk(distance, distances, water_drunk, water_timestamps)
        log_raw_data(distance, distance_timestamps, distances)
        print(f"timestamps: {list(zip(distance_timestamps, distances))}")
        print(f"timestamps: {list(zip(water_timestamps, water_drunk))}")
        print('-' * 140)
        sleep(2)