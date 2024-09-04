import json
from channels.generic.websocket import WebsocketConsumer

class DocumentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        # Broadcast content to all clients
        self.send(text_data=json.dumps({
            'content': content
        }))
