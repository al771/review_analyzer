class ComparisonService:
    def compare_results(self, ninja_result, twinword_result):
        agreement = self._determine_agreement(ninja_result, twinword_result)


        better = self._choose_better_result(ninja_result, twinword_result)

        if agreement:
            final_sentiment = ninja_result["sentiment"]
        else:
            final_sentiment = better["sentiment"]

        conclusion_text = self._format_conclusion(agreement, better)

        return {
            "agreement": agreement,
            "conclusion_text": conclusion_text,
            "final_sentiment": final_sentiment,
            "better_service": better.get("service", "unknown")
        }
    def _determine_agreement(self, result1, result2):
        if result1["success"] and result2["success"]:
            if result1["sentiment"] == result2["sentiment"]:
                return True

        return False

    def _choose_better_result(self, result1, result2):
        if result1["success"] and not result2["success"]:
            return result1
        if result2["success"] and not result1["success"]:
            return result2

        if result2["success"] and result1["success"]:

            if result1["score"] >= result2["score"]:
                return result1
            else:
                return result2

        return {"sentiment": "unknown", "service": "none", "success": False}


    def _format_conclusion(self, agreement, better_result):
        if agreement and better_result["success"]:
            return f"Сервисы согласны: {better_result['sentiment'].upper()}"
        elif not agreement and better_result["success"]:
            service_name = better_result.get("service", "неизвестный сервис")
            return f"Сервисы расходятся. Лучший: {service_name}"
        else:
            return "Ошибка: сервисы недоступны"



