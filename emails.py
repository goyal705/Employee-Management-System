import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymongo
import time
from datetime import datetime
import os

usernamedb=os.getenv('usernamedb')
password=os.getenv('password')

def extractdata():
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection = db["Emails"]
    response=collection.find_one({})
    client.close()
    return response["data"]

def removedata(data):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection = db["Emails"]
    update_query = {"$pull":{"data": data}}
    response=collection.update_one({},update_query)
    print("Removed email data:",data["recipientmail"])
    client.close()

def sendmail():
    data=extractdata()
    for i in data:
        start=time.time()
        recipient=i["recipientmail"]
        subject=i["subject"]
        body=i["body"]
        
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
        removedata(i)
        end=time.time()
        print("Time taken: ",end-start)
    

while True:
    try:
        sendmail()
    except Exception as err:
        print(err)
