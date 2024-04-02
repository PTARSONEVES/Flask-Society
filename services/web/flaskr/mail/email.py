import smtplib, ssl, os
from flask import current_app 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


def sendmail(email,subject,html):

    port = current_app.config["MAIL_PORT"]
    smtp_server = current_app.config["MAIL_SERVER"]
    sender_email = current_app.config["MAIL_USERNAME"]
    password = current_app.config["MAIL_PASSWORD"]

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject + str(datetime.now())
    msg['From'] = current_app.config["MAIL_USERNAME"]
    msg['To'] = email

    # Create the body of the message (a plain-text and an HTML version).
    text = "Olá!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')


    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

#    try:
    print('FASE 1')
    mail = smtplib.SMTP(smtp_server, port)
    mail.ehlo()
    print('FASE 2')
    mail.starttls()
    print('LOGIN...')
    mail.login(sender_email, password)
    mail.sendmail(sender_email, email, msg.as_string())
    mail.quit()
    print('Email enviado com sucesso!!!')
#    except:

def sendpdf(email,file,subject):

    port = current_app.config["MAIL_PORT"]
    smtp_server = current_app.config["MAIL_SERVER"]
    sender_email = current_app.config["MAIL_USERNAME"]
    password = current_app.config["MAIL_PASSWORD"]

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart()
    msg['Subject'] = subject + 'mensagem enviada em ' + str(datetime.now())
    msg['From'] = current_app.config["MAIL_USERNAME"]
    msg['To'] = email

    # Create the body of the message (a plain-text and an HTML version).
    text = subject

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')

    binary_pdf = open(file,'rb')
    print('FILE: ',file)
    print('BINARIO: ',binary_pdf)
    payload= MIMEBase('application','octate-stream',Name=file)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition','attachment',filename=file)

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(payload)

#    try:
    mail = smtplib.SMTP(smtp_server, port)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, password)
    mail.sendmail(sender_email, email, msg.as_string())
    mail.quit()
#    except:

