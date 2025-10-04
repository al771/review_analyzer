from typing import Dict, Any
def compare_results(ninja_result: Dict[str, Any], twinword_result: Dict[str, Any]) -> Dict[str, Any]:
    """Сравнивает результаты двух API и формирует итоговый анализ"""
    agreement: bool = _determine_agreement(ninja_result, twinword_result)
    better: Dict[str, Any] = _choose_better_result(ninja_result, twinword_result)

    if agreement:
        final_sentiment: str = ninja_result["sentiment"]
    else:
        final_sentiment = better["sentiment"]

    conclusion_text: str = _format_conclusion(agreement, better)

    return {
        "agreement": agreement,
        "conclusion_text": conclusion_text,
        "final_sentiment": final_sentiment,
        "better_service": better.get("service", "неизвестный")
    }
def _determine_agreement(result1: Dict[str, Any], result2: Dict[str, Any]) -> bool:
    """Проверяет согласие сервисов по тональности"""
    if result1["success"] and result2["success"]:
        if result1["sentiment"] == result2["sentiment"]:
            return True
    return False
def _choose_better_result(result1: Dict[str, Any], result2: Dict[str, Any]) -> Dict[str, Any]:
    """Выбирает лучший результат по уверенности и успешности"""
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

def _format_conclusion(agreement: bool, better_result: Dict[str, Any]) -> str:
    """Формирует текст заключения для отображения"""
    if agreement and better_result["success"]:
        return f"Сервисы согласны: {better_result['sentiment'].upper()}"
    elif not agreement and better_result["success"]:
        service_name: str = better_result.get("service", "неизвестный сервис")
        return f"Сервисы расходятся. Лучший: {service_name}"
    else:
        return "Ошибка: сервисы недоступны"