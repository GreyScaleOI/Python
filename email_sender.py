import smtplib
import ssl
from email.message import EmailMessage
from app2 import password

email_sender = 'xyz@gmail.com'
email_password = password
email_receiver = 'bac@gmail.com'
subject = "Creation of a emailing script"
body = ''' Hope you'll hire me '''

em= EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())