from typing import Dict, Any
import config
from services.base_service import BaseService

class TwinwordService(BaseService):
    # Сервис для анализа тональности через Twinword API
    def __init__(self) -> None:
        super().__init__("twinword", config.TWINWORD_URL, config.TWINWORD_HOST)

    def _get_api_key(self) -> str:
        # Получает ключ из конфига
        return config.RAPIDAPI_KEY

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        # Анализирует тональность
        try:
            data: Dict[str, Any] = self._make_request(text)

            if data["result_code"] == "200":
                return self._normalize_response(data)
            else:
                return {
                    "error": f"API ошибка: {data.get('result_msg', 'Неизвестная ошибка')}",
                    "service": self.service_name,
                    "success": False
                }

        except Exception as e:
            return {
                "error": str(e),
                "service": self.service_name,
                "success": False
            }

    def _normalize_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Нормализует ответ
        return {
            "score": abs(float(data["score"])),
            "sentiment": data["type"],
            "service": self.service_name,
            "success": True
        }