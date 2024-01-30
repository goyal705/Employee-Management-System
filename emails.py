import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime
import os

usernamedb=os.getenv('usernamedb')
password=os.getenv('password')

def sendmailprod(data):
        start=time.time()
        recipient=data["recipientmail"]
        subject=data["subject"]
        body=data["body"]
        
        email = "tushargoyal628@outlook.com"
        password = os.getenv('outlook')
        
        message = MIMEMultipart()
        message["From"] = email
        message["To"] = recipient
        message["Subject"] = subject

        message.attach(MIMEText(body, "html"))

        smtp_server = "smtp.office365.com"
        smtp_port = 587

        context = ssl.create_default_context()

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(email, password)
            server.sendmail(email, recipient, message.as_string())

        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Email sent successfully to {recipient} at {time_string}")
        # removedata(i)
        end=time.time()
        print("Time taken: ",end-start)
