from threading import Thread

from main import main
from backend import start_server
from reminder import reminder


if __name__ == "__main__":
    water_timestamps = []
    water_drunk = []
    distances = [] 
    distance_timestamps = []
    Thread(target=main).start()
    Thread(target=start_server).start()
    Thread(target=reminder).start()

