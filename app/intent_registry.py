# intent_registry.py

from loguru import logger

# Dictionary to store intent-function mappings
INTENT_FUNCTIONS = {}

def register_intent(intent_name):
    """
    Decorator to register intent functions.
    """
    def decorator(func):
        INTENT_FUNCTIONS[intent_name] = func
        logger.info(f"Registered intent: {intent_name}")
        return func
    return decorator
