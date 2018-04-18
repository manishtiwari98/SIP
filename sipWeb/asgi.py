import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecellSip.settings")
channel_layer = channels.asgi.get_channel_layer()