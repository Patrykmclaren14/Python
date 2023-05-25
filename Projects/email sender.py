from email.message import EmailMessage
from email_counter import password
import ssl
import smtplib

email_sender = 'wierzbowskipatryk0@gmail.com'
email_password = password

email_reciver = 'tofisir594@necktai.com'


subject = "HELLO EVERYBODY"
body = """
It is my first message. IS TEST!!!
"""

em = EmailMessage()        # tworzy wiadomosc
em['From'] = email_sender  # skad
em['To'] = email_reciver   # do
em['subject'] = subject    # wiadomosc
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
