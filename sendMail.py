import getpass
import smtplib
from email.mime.text import MIMEText

def sendMail():
    print("Enter your password")
    sender_add = 'afram.p245@gmail.com'
    password = getpass.getpass()
    subject = "Learn.Inspire.Grow"
    msg = ''' 
    Hello everyone!
    We are pleased to announce that we are going to start a new batch  
    of AI Mafia. Hope you join.
    
    Thank you
    Afra
    '''
    server  = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(sender_add, password)
    
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_add
    msg['To'] = 'afrakllk@gmail.com'
    msg.set_param('importance', 'high value')
    recipients = 'afrakllk@gmail.com'
    server.sendmail(msg['From'], recipients, msg.as_string())
sendMail()
