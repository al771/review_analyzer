from typing import Dict, Any


def compare_results(r1: Dict[str, Any], r2: Dict[str, Any]) -> Dict[str, Any]:
    # Сравнивает два нормализованных результата и формирует итог
    agreement = r1["success"] and r2["success"] and (r1["sentiment"] == r2["sentiment"])
    better = _choose_better_result(r1, r2)
    final_sentiment = r1["sentiment"] if agreement else better["sentiment"]
    conclusion_text = _format_conclusion(agreement, better)
    return {
        "agreement": agreement,
        "conclusion_text": conclusion_text,
        "final_sentiment": final_sentiment,
        "better_service": better.get("service", "unknow"),
    }

def _choose_better_result(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    # Выбирает лучший результат
    if a["success"] and not b["success"]:
        return a
    if b["success"] and not a["success"]:
        return b
    if a["success"] and b["success"]:
        return a if a["score"] >= b["score"] else b
    # если оба неуспешны
    return {"sentiment": "unknown", "service": "none", "success": False, "score": 0.0}

def _format_conclusion(agreement: bool, better: Dict[str, Any]) -> str:
    # Формирует текст результата
    if agreement and better.get("success"):
        return f"Сервисы согласны: {better['sentiment'].upper()}"
    elif not agreement and better.get("success"):
        name = better.get("service", "неизвестный сервис")
        return f"Сервисы расходятся. Лучший: {name}"
    else:
        return "Ошибка: сервисы недоступны"
