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

        for filename in image_filenames:
            with open(os.path.join(self.path,filename), "rb") as file:
                self.frames.append(file.read())
        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.03)
                
class FrameSenderUnet(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()
        
        self.frames = []
        self.path = "demo/unet/"
        image_filenames = os.listdir(self.path)
        
        def extract_number(filename):
            match = re.search(r'(\d+)', filename)
            return int(match.group()) if match else 0
        image_filenames = sorted(image_filenames, key=extract_number)

        for filename in image_filenames:
            with open(os.path.join(self.path,filename), "rb") as file:
                self.frames.append(file.read())
        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.03)
                
class FrameSenderASR(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()
        
        self.frames = []
        self.path = "demo/asr/"
        image_filenames = os.listdir(self.path)
        
        def extract_number(filename):
            match = re.search(r'(\d+)', filename)
            return int(match.group()) if match else 0
        image_filenames = sorted(image_filenames, key=extract_number)

        for filename in image_filenames:
            with open(os.path.join(self.path,filename), "rb") as file:
                self.frames.append(file.read())
        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.06)