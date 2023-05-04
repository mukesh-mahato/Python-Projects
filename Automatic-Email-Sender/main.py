# Import the required libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Read the email addresses and message content from a CSV file
data = pd.read_csv('email_data.csv')
sender_email = 'your_email_address@gmail.com'
sender_password = 'your_email_password'
subject = 'Automated Email'
message = 'Hello, this is an automated email.'

# Create a function to connect to the SMTP server and log in to the sender's email account
def connect_to_server():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    return server

# Create a function to send the emails to the recipients
def send_email(server, recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)

# Loop through the recipients' email addresses and send the emails
server = connect_to_server()
for email in data['Email']:
    send_email(server, email, subject, message)
server.quit()
