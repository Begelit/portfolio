"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from mainapp.consumer import FrameSenderInfocen,FrameSenderUnet,FrameSenderASR,FrameSenderCV,FrameSenderLLM

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("framesender/infocen/", FrameSenderInfocen.as_asgi()),
                path("framesender/unet/", FrameSenderUnet.as_asgi()),
                path("framesender/asr/", FrameSenderASR.as_asgi()),
                path("framesender/cv/", FrameSenderCV.as_asgi()),
                path("framesender/llm/", FrameSenderLLM.as_asgi())


                # path("chat/admin/", AdminChatConsumer.as_asgi()),
                # path("chat/", PublicChatConsumer.as_asgi()),
            ])
        )
    ),
})