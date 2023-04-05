import json
from channels.generic.websocket import WebsocketConsumer
from time import sleep
import requests


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        self.send(text_data=json.dumps({
            'type': 'connection JAJA established',
            'message': 'you are now connected!'
        }))


    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        print("Mesage: ", message)
        
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
        
        
class ApiConsumer(WebsocketConsumer):
    flag = True
    
    def connect(self):
        self.accept()
        
        self.send(text_data=json.dumps({
            "type": 'connection',
           "message": 'You connected successfully to apiRest'
        }))
        
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print("MENSAJE: ", text_data_json)
        code = text_data_json['message']
        
        try:
            r = requests.get(url = 'http://127.0.0.1:8001/api/products/' + code)
            # print('RESPONSE: ', r.json())
            self.send(text_data=json.dumps({
                'type': 'product',
                'message': r.json()
            }))
        except Exception as e:
            print(e)
            self.close()
        
        
    def disconnect(self, code):
        self.close()