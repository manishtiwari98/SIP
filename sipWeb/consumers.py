from channels import Group
from django.http import HttpResponse
from channels.handler import AsgiHandler
import json

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

def ws_message(message):
    data=json.loads(message['text'])
    
    name=data['name']
    location=data['location']
    description=data['description']
    no_of_position=data['no_of_position']
    stipend=data['stipend']
    position=data['position']
    
    Group("chat").send({
        "text": json.dumps({'name':name,'location':location,'description':description,'no_of_position':no_of_position,'stipend':stipend,'position':position}) 
    
    })


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)