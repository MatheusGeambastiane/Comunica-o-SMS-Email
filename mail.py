import smtplib 
import email.message
from unicodedata import name
from env import passwd, email as frommail

#TODO: Configurar o dotenv

def send_mail(mail, keypas):
    body = """
    <p> Email function </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Email function"
    msg ['From'] = mail
    msg ['To'] = 'matheuscdc111lol@gmail.com'
    password = keypas
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except Exception as e:
        print(e)


send_mail(frommail, passwd)
