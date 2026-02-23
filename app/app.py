import os
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import requests

load_dotenv()

WPP_API_URL = os.getenv("WPP_API_URL")
WPP_TOKEN = os.getenv("WPP_TOKEN")
WPP_SESSION = os.getenv("WPP_SESSION")

headers = {
        "Authorization": f"Bearer {WPP_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


@asynccontextmanager
def lifespan(app: FastAPI):
    url = f"{WPP_API_URL}/api/{WPP_SESSION}/start-session"

    payload = Dict[str, Any] = {
        "webhook": "http://localhost:8000/webhook",
        "waitQrCode": False,
        "jsonSchemaWebhook": True
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        print(f"Session start response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error starting session: {e}")
        raise e
    yield

    print("Shutting down session...")

app = FastAPI(lifespan=lifespan)

app.post("/webhook")
async def whatsapp_webhook(request: Request):
    body = await request.json()
    print(f"Received webhook: {body}")

    try:
        messages = body.get("messages", []) or body.get("data", [])
        for msg in messages:
            phone = msg.get("phone") or msg.get("from")
            text = msg.get("body") or msg.get("message")
            if not phone or not text:
                continue 
            send_wpp_message(phone, f"""Olá! Recebemos sua mensagem: '{text}'. Em breve entraremos em contato!""")
    except Exception as e:
            print(f"Error processing webhook: {e}")
    
    return JSONResponse(content={"status": "success"}, status_code=200)


def send_wpp_message(phone: str, message: str, is_group: bool = False):
    url = f"{WPP_API_URL}/send-message"

    payload = {
        "phone": phone,
        "message": message,
        "isGroup": is_group
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Sent message to {phone}: {response.status_code} - {response.text}")
    return response

