import config
import requests
from config import RAPIDAPI_KEY, NINJA_URL, NINJA_HOST

class NinjaService:
    def __init__(self):
        self.api_key = config.RAPIDAPI_KEY
        self.url = config.NINJA_URL
        self.host = config.NINJA_HOST
    def analyze_sentiment(self, text):
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host
        }
        url = self.url
        params = {"text": text}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return self.normalize_response(data)
        return {"error": f"status {response.status_code}", "service": "ninja", "success": False}

    def normalize_response(self, data):
        return {"score": data["score"],
                "sentiment": data["sentiment"].lower(),
                "service": "ninja",
                "success": True
                }

