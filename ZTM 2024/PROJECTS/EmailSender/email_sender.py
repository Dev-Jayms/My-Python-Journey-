# This Python script is using the `smtplib` and `ssl` modules to send an outlook email via an SMTP server.
# Here's a breakdown of what the script is doing:
import smtplib, ssl
# from email.message import EmailMessage
def email_sender():
    port = 587
    smtp_server = "smtp.office365.com"
    sender_email = "jameskonomanyi@outlook.com"
    # password = "MyFamily4JesusChrist."
    receiver_email = "jameskonomanyi@gmail.com"
    message = """\
    Subject: Hi James

    This message is sent from James Python script."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login("jameskonomanyi@outlook.com", "Jay&$#1234_&(Kay).")
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent!")
email_sender()