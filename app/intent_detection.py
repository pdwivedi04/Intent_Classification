import spacy
from loguru import logger

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Define intent-based keywords
INTENT_MAP = {
    "repeat": ["repeat the question", "repeat again", "repeat it", "ask again", "ask it again", "could you please repeat the question?", "could you please repeat again?", "could you please repeat it?", "could you please ask again?", "could you please ask it again?"],
    "skip": ["skip", "skip it", "skip this question","please skip this one", "please skip", "next question", "please ask next question", "please ask the next question", "please ask the next one", "next one", "next"],
    "exit": ["exit", "quit", "goodbye", "bye", "stop", "end", "finish", "close", "shut down", "shut up"],
}

def detect_intent(transcribed_text):
    """
    Identifies the user's intent from the transcribed text.
    :param transcribed_text: The text obtained from speech-to-text.
    :return: Identified intent (str)
    """
    logger.info(f"Processing intent for text: {transcribed_text}")
    text_lower = transcribed_text.lower()

    for intent, keywords in INTENT_MAP.items():
        if any(word in text_lower for word in keywords):
            logger.info(f"Detected intent: {intent}")
            return intent

    logger.warning("No matching intent found. Defaulting to 'unknown'.")
    return "unknown"
