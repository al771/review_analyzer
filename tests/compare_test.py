from src.services.ninja_service import NinjaService
from src.services.twinword_service import TwinwordService
from src.services.comparison_service import ComparisonService

ninja = NinjaService()
twinword = TwinwordService()
comparison = ComparisonService()

text = "This movie is okay, nothing special"

ninja_result = ninja.analyze_sentiment(text)
twinword_result = twinword.analyze_sentiment(text)
comparison_result = comparison.compare_results(ninja_result, twinword_result)

print(f"Ninja: {ninja_result}")
print(f"Twinword: {twinword_result}")
print(f"Comparison: {comparison_result}")