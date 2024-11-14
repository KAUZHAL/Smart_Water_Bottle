from pywhatkit import sendwhatmsg_instantly
import schedule
import time

def water_alert(phno):
    sendwhatmsg_instantly(phno, "Its time for a water break.", 15)
    print("Sent message.")

if __name__ == "__main__":
    phno = '+8840413659'
    schedule.every(60).minutes.do(lambda: water_alert(phno))
    while True:
        schedule.run_pending()
        time.sleep(1)