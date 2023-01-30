from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from lots.models import Lot


class LotConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['lot_id']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        Lot.objects.filter(id=int(self.group_name), price__lt=int(text_data))\
            .update(price=int(text_data))
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'change_price',
            'price': str(Lot.objects.get(id=int(self.group_name)).price)
        })

    def change_price(self, event):
        self.send(event['price'])
