import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests

load_dotenv()

WPP_API_URL = os.getenv("WPP_API_URL")
WPP_TOKEN = os.getenv("WPP_TOKEN")
WPP_SESSION = os.getenv("WPP_SESSION")

app = FastAPI()


def wpp_headers():
    return {
        "Authorization": f"Bearer {WPP_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
 
def send_wpp_message(phone_number: str, message: str, is_group: bool = False):
    url = f"{WPP_API_URL}/send-message"

    payload = {
        "phone": phone_number,
        "message": message,
        "isGroup": is_group
    }
    response = requests.post(url, headers=wpp_headers(), json=payload)
    print(f"Sent message to {phone_number}: {response.status_code} - {response.text}")
    return response

