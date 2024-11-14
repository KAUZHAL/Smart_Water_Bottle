from user_data import log_raw_data, dummy_sensor, amount_drunk
from time import sleep
from plot import plot_data

bottle_radius = 4.25 # In cm
bottle_height = 16.5 # In cm

bottle_volume = 936.5 # In ml

def main(water_timestamps, water_drunk, distances, distance_timestamps):
    distance = next(dummy_sensor())
    amount_drunk(distance, distances, water_drunk, water_timestamps)
    log_raw_data(distance, distance_timestamps, distances)
    
    print(f"timestamps: {list(zip(distance_timestamps, distances))}")
    print(f"timestamps: {list(zip(water_timestamps, water_drunk))}")

    with open('xydb.txt', 'w') as f:
        f.writelines((str(water_timestamps), str(water_drunk)))

    print('-' * 140)
    sleep(2)


if __name__ == "__main__":
    water_timestamps = []
    water_drunk = []
    distances = [] 
    distance_timestamps = []

    for i in range(10):
        main(water_timestamps, water_drunk, distances, distance_timestamps)
    
    plot_data(water_timestamps, water_drunk)
