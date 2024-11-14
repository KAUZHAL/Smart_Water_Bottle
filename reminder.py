from pywhatkit import sendwhatmsg_instantly
from datetime import datetime
def reminder():
    prev_time = -1
    while True:
        sendwhatmsg_instantly("+9462939442", "Its time for a water break.", 15)