from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import os
import time
import re
import asyncio

class getFramesClass:
    def __init__(self,path):
        self.frames = []
        self.path = path
        self.image_filenames = os.listdir(self.path)
        self.image_filenames = sorted(self.image_filenames, key=self.extract_number)
        
    @staticmethod
    def extract_number(filename):
        match = re.search(r'(\d+)', filename)
        return int(match.group()) if match else 0
    
    def getFrames(self):
        for filename in self.image_filenames:
            with open(os.path.join(self.path,filename), "rb") as file:
                self.frames.append(file.read())
        return self.frames
    
infocen_frames = getFramesClass("demo/infocen/").getFrames()
unet_frames = getFramesClass("demo/unet/").getFrames()
asr_frames = getFramesClass("demo/asr/").getFrames()
cv_frames = getFramesClass("demo/cv/").getFrames()
llm_frames = getFramesClass("demo/llm/").getFrames()

    
class FrameSenderInfocen(AsyncWebsocketConsumer):

    async def connect(self):
        global infocen_frames

        await self.accept()
        
        self.frames = infocen_frames#getFramesClass("demo/infocen/").getFrames()

        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.03)
                
class FrameSenderUnet(AsyncWebsocketConsumer):

    async def connect(self):
        global unet_frames

        await self.accept()
        
        self.frames = unet_frames#getFramesClass("demo/unet/").getFrames()

        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.03)
                
class FrameSenderASR(AsyncWebsocketConsumer):

    async def connect(self):
        global asr_frames
        await self.accept()
        
        self.frames = asr_frames#getFramesClass("demo/asr/").getFrames()

        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.06)
                
class FrameSenderCV(AsyncWebsocketConsumer):

    async def connect(self):
        global cv_frames

        await self.accept()
        
        self.frames = cv_frames#getFramesClass("demo/cv/").getFrames()
        self.path = "demo/cv/"

        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.06)
            
class FrameSenderLLM(AsyncWebsocketConsumer):

    async def connect(self):
        global llm_frames

        await self.accept()
        
        self.frames = llm_frames#getFramesClass("demo/llm/").getFrames()

        self.count = 0

        while True:
            for frame in self.frames:
                await self.send(bytes_data=frame)
                await asyncio.sleep(0.06)