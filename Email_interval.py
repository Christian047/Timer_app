#Create a project that will send an automatic email every 10mins 
# We imported modules to help us run the code
import smtplib
from email.message import EmailMessage
import datetime
import time
def send_email():

# Set up email credentials
 sender_email = 'ugwudavidejeh@gmail.com'
 email_password = 'heagnrthwlblyirk'
 recipient_email = 'callistus100@gmail.com'
 subject = 'automatic email'
 
# we called an object of the EmailMessage class
 email_msg = EmailMessage()

 email_msg['Subject'] = subject
 email_msg['From'] = sender_email
 email_msg['To'] = recipient_email
 email_msg.set_content(f'This is an automatic email sent at {datetime.datetime.now()}')
 

# We opened a secure smtp server, at smtp.gmail.com,at port 465
 with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, email_password)
    smtp.send_message(email_msg)
    print('email sent')
    
# We used a while loop function to send repeated emails
while True:
    send_email()
# we used a time.sleep method to send at different intervals
    time.sleep(600)