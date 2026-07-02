"""
emotion_detection.py

This module provides a function to detect emotions from text
using the Watson NLP EmotionPredict API.
"""

from watson_nlp import EmotionPredict


# Load the pretrained emotion model
emotion_model = EmotionPredict.load("emotion_aggregated-workflow_lang_en_stock")


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text.

    Args:
        text_to_analyze (str): Input text.

    Returns:
        dict: Dictionary containing emotion scores.
    """
    response = emotion_model.predict(text_to_analyze)

    return {
        "anger": response["emotion"]["anger"],
        "disgust": response["emotion"]["disgust"],
        "fear": response["emotion"]["fear"],
        "joy": response["emotion"]["joy"],
        "sadness": response["emotion"]["sadness"],
        "dominant_emotion": max(
            response["emotion"],
            key=response["emotion"].get
        )
    }
