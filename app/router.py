from loguru import logger
from app.intent_registry import register_intent

@register_intent("repeat")
def handle_repeat():
    print("⏭️ Repeating this question.")
    

@register_intent("skip")
def handle_skip():
    print("⏭️ Skipping this question.")

@register_intent("exit")
def handle_exit():
    raise ExitIntent  # This will stop execution and break the loop

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
    
    return "Thanks, I got your response."


class ExitIntent(Exception):
    """Custom exception to handle exit intent."""
    pass


