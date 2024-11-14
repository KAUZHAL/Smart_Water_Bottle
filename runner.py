from threading import Thread

from main import main
from backend import start_server
from reminder import water_alert

if __name__ == "__main__":
    water_timestamps = []
    water_drunk = []
    distances = [] 
    distance_timestamps = []

    phone_number = "+8840413659"

    Thread(target=main, args=(water_timestamps, water_drunk, distances, distance_timestamps)).start()
    Thread(target=start_server).start()
    Thread(target=water_alert, args=(phone_number, )).start()

