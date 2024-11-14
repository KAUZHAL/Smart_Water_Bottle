from pywhatkit import sendwhatmsg_instantly
from datetime import datetime

def reminder():
    prev_time = -1
    while True:
        hour = datetime.now().hour
        if hour != prev_time:
            # sendwhatmsg_instantly("+9462939442", "Its time for a water break.", 15)
            print("hello")
            prev_time = hour
