import os
import requests
from dotenv import load_dotenv

load_dotenv()

def analyze_log_with_gemini(log_data):
    API_KEY = os.getenv("GEMINI_API_KEY")
    prompt = f"Berikan analisis singkat dari log berikut dan rekomendasi:\n{log_data}"

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}",
        json={
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
    )

    if response.status_code == 200:
        return (
            response.json()
            .get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "Tidak ada respon.")
        )
    else:
        return f"Error dari Gemini: {response.status_code} - {response.text}"
