import time
import random

def analyze_japanese_text(text, culture, relationship, purpose):
    """
    Mock AI analysis returning formal metrics and suggestions.
    """
    # Simulate network delay (5-10s per TR-04, but let's use 2s for better UX in demo)
    time.sleep(2)
    
    return {
        "formality": random.randint(40, 95),
        "naturalness": random.randint(50, 90),
        "relevance": random.choice(["High", "Medium", "Low"]),
        "overall": "The sentence is understandable but could be improved for a workplace setting.",
        "culture_explanation": "In Japanese workplace culture, using Keigo (honorifics) is essential when talking to a superior. The current sentence sounds a bit too direct.",
        "rewrite_suggestions": [
            "お忙しいところ恐れ入りますが、...",
            "もしよろしければ、..."
        ],
        "related_expressions": [
            "ご確認のほどよろしくお願いいたします。",
            "お手数をおかけしますが、..."
        ]
    }
