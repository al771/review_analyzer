from abc import ABC, abstractmethod
from typing import Dict, Any


class SentimentAnalyzer(ABC):
    """Абстрактный базовый класс для анализа тональности"""

    def __init__(self, service_name: str, api_url: str, host: str) -> None:
        """Инициализация анализатора тональности"""
        self.service_name: str = service_name
        self.api_url: str = api_url
        self.host: str = host
        self.api_key: str = self._get_api_key()

    @abstractmethod
    def _get_api_key(self) -> str:
        """Получает API ключ из конфигурации"""
        pass

    @abstractmethod
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Анализирует тональность текста"""
        pass
    @abstractmethod
    def _normalize_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Нормализует ответ API к стандартному формату"""
        pass
    def _make_request(self, text: str) -> Dict[str, Any]:
        """Выполняет HTTP запрос к API"""
        import requests

        headers: Dict[str, str] = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host
        }
        params: Dict[str, str] = {"text": text}

        try:
            response = requests.get(self.api_url, params=params, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"HTTP ошибка {response.status_code}")

        except requests.RequestException as e:
            raise Exception(f"Сетевая ошибка: {str(e)}")