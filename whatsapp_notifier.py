import os
import requests

def send_whatsapp_notification(message):
    API_KEY = os.getenv("FONNTE_API_KEY")
    PHONE = os.getenv("PHONE_NUMBER").split(",")

    headers = {
        "Authorization": API_KEY
    }

    data = {
        "target": PHONE,
        "message": message
    }

    response = requests.post("https://api.fonnte.com/send", headers=headers, data=data)
    print(f"WhatsApp status: {response.status_code}")
    print(f"[DEBUG] Fonnte Response Text: {response.text}")
