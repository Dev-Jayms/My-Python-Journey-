# '''I created an email sender with python from the email module, this will send email with html embedded'''

import smtplib, ssl
from email.message import EmailMessage

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "jameskonomanyi@gmail.com"
password = "MyFamily4JesusChrist."
receiver_email = "mrjameskonomanyi@gmail.com"
message = """\
Subject: Hi there

This message is sent from James Python script."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login("jameskonomanyi@gmail.com", "Jay&$#1234_&(Kay).")
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent!")




# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path


# # The function below is created to send an email:
# def email_sender():
#     html = Template(Path("index.html").read_text())
#     email=EmailMessage()
#     email["from"] = "Mr James Konomanyi"
#     email["to"] = "jameskonomanyi@gmail.com"
#     email["subject"] = "Python email sender"

#     email.set_content(html.substitute({"name":"Jayms"}),html)

#     with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login(user="mrjameskonomanyi@gmail.com", password="MyFamily4JesusChrist")
#         smtp.send_message(email)
#         print("Message sent!!")
# email_sender()