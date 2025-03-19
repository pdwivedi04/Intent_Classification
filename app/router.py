from loguru import logger

def handle_repeat():
    return "Fetching the current weather for you... ☁️"

def handle_skip():
    from datetime import datetime
    return f"The current time is {datetime.now().strftime('%H:%M:%S')} ⏰"

def handle_exit():
    return "Goodbye! Have a great day! 👋"

# Intent-Function Mapping
INTENT_FUNCTIONS = {
    "repeat": handle_repeat,
    "skip": handle_skip,
    "exit": handle_exit,
}

def route_intent(intent):
    """
    Routes the detected intent to the corresponding function.
    :param intent: The detected intent (string)
    :return: Response from the mapped function.
    """
    logger.info(f"Routing intent: {intent}")
    if intent in INTENT_FUNCTIONS:
        return INTENT_FUNCTIONS[intent]()
    
    return "Sorry, I didn't understand that. Can you repeat? 🤔"
