from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class LotConsumer(WebsocketConsumer):
    def connect(self):
        # self.group_name = 'all'
        # async_to_sync(self.channel_layer)
        self.accept()
        print('connected')

    def disconnect(self, code):
        print('disconnected')
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass
