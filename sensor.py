import serial
import time

arduino = serial.Serial('COM5', 9600) 
time.sleep(2)  

def read_ultrasonic_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()
            if "Distance:" in data:
                distance = int(data.split(" ")[1])
                yield(distance)

if __name__ == "__main__":
    print("Starting to read ultrasonic data from Arduino...")
    try:
        read_ultrasonic_data()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        arduino.close()
