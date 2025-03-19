import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
from datetime import datetime
from loguru import logger

# Set up logging
LOGS_DIR = "../logs"
os.makedirs(LOGS_DIR, exist_ok=True)
logger.add(os.path.join(LOGS_DIR, "app.log"), rotation="1 MB")

# Whisper Model
MODEL = whisper.load_model("base")  # Use "tiny", "small", or "medium" if needed

def transcribe_audio(file_path):
    """
    Transcribes the given audio file using Whisper.
    :param file_path: Path to the audio file.
    :return: Transcribed text.
    """
    logger.info(f"Transcribing audio file: {file_path}")
    result = MODEL.transcribe(file_path)
    return result["text"]


