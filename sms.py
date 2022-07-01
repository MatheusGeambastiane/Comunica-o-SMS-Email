import os
from twilio.rest import Client
from env import auth_token, sid


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = sid
authtoken = auth_token
client = Client(account_sid, authtoken)

def send_sms(text, contact):
    message = client.messages.create(
                                body=text,
                                from_='+19895752436',
                                to=contact
                            )   
    print(message.sid)  
    print('Enviado')

mensagem = 'Msg'
contato = '+5571992997191'

send_sms(mensagem, contato)