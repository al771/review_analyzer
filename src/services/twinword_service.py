import config
import requests
from config import RAPIDAPI_KEY, TWINWORD_URL, TWINWORD_HOST

class TwinwordService:
    def __init__(self):
        self.api_key = config.RAPIDAPI_KEY
        self.url = config.TWINWORD_URL
        self.host = config.TWINWORD_HOST
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
            if data["result_code"] == "200":
                return self.normalize_response(data)
            else:
                return {"error": data.get("result_msg", "API error"), "service": "twinword", "success": False}
        return {"error": f"status {response.status_code}", "service": "twinword", "success": False}

    def normalize_response(self, data):
        return {"score": data["score"],
                "sentiment": data["type"],
                "service": "twinword",
                "success": True
                }

