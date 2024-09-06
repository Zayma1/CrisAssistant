from twilio.rest import Client
from flask import Flask, request
from twilio.http.http_client import TwilioHttpClient
import certifi
import requests

app = Flask(__name__)


#account_sid = 'id'
#auth_token = 'token'

class CustomTwilioHttpClient(TwilioHttpClient):
    def __init__(self):
        super().__init__()
        self.session.verify = certifi.where()


client = Client(account_sid, auth_token, http_client=CustomTwilioHttpClient())

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    print(request.values)
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')
    to_number = request.values.get('To', '')
    num_media = int(request.values.get('NumMedia', 0))

    if num_media > 0:
        mediaURL = request.values.get('MediaUrl0')
        media_type = request.values.get('MediaContentType0')

        if "audio" in media_type:
            audio_data = requests.get(mediaURL,auth=(account_sid,auth_token)).content
            
            with open('audio_message.wav', 'wb') as f:
                f.write(audio_data)


    response_msg = ''
    if 'oi' in incoming_msg:
        response_msg = 'Olá! Como posso te ajudar?'
    elif 'info' in incoming_msg:
        response_msg = 'Eu sou um bot criado usando Python e Twilio!'

    try:
        # Enviar resposta usando Twilio API
        message = client.messages.create(
            body=response_msg,
            from_=to_number,
            to=from_number
        )
        return "Message sent", 200
    except Exception as e:
        return f"Failed to send message: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
