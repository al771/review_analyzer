from typing import Dict, Any
import config
from services.base_service import BaseService
class NinjaService(BaseService):
    # Сервис для анализа тональности через API Ninjas

    def __init__(self) -> None:
        super().__init__("ninja", config.NINJA_URL, config.NINJA_HOST)
    def _get_api_key(self) -> str:
        return config.RAPIDAPI_KEY
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        try:
            data: Dict[str, Any] = self._make_request(text)
            return self._normalize_response(data)
        except Exception as e:
            return {
                "error": str(e),
                "service": self.service_name,
                "success": False
            }

    def _normalize_sentiment(self, raw_sentiment: str) -> str:
        sentiment = raw_sentiment.lower()
        if "positive" in sentiment:
            return "positive"
        elif "negative" in sentiment:
            return "negative"
        else:
            return "neutral"

    def _normalize_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "score": abs(float(data["score"])),
            "sentiment": self._normalize_sentiment(data["sentiment"]),
            "service": self.service_name,
            "success": True
        }