from src.services.ninja_service import NinjaService

service = NinjaService()

result = service.analyze_sentiment("Terrible movie")
print(result)