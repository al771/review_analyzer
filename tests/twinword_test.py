from src.services.twinword_service import TwinwordService

service = TwinwordService()

result = service.analyze_sentiment("Ужасный фильм")
print(result)