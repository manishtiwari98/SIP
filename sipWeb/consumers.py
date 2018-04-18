from channels import Group
from django.http import HttpResponse
from channels.handler import AsgiHandler
import json

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

def ws_message(message):
    Group("chat").send({
        "text": json.dumps({'name':'Manish'}) 
    })


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)