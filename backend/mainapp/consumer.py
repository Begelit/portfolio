from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import os
import time
import re
import asyncio

class FrameSenderInfocen(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()
        
        self.frames = []
        self.path = "demo/infocen/"
        image_filenames = os.listdir(self.path)
        
        def extract_number(filename):
            match = re.search(r'(\d+)', filename)
            return int(match.group()) if match else 0
        image_filenames = sorted(image_filenames, key=extract_number)
        # print(image_filenames)
        # print(len(image_filenames))
        for filename in image_filenames:
            with open(os.path.join(self.path,filename), "rb") as file:
                self.frames.append(file.read())
        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.03)

        # self.accept("subprotocol")
        
        # self.close()

    # def receive(self, text_data=None, bytes_data=None):

    #     self.send(text_data="Hello world!")

    #     self.send(bytes_data="Hello world!")

    #     self.close()

    #     self.close(code=4123)

    # def disconnect(self, close_code):
        # Called when the socket closes