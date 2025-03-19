from app.audio_processing import record_audio
from app.speech_to_text import transcribe_audio


def main():
    
    print("🎙 Starting real-time speech-to-text...")
    audio_file = record_audio()  # Record until silence is detected
    print("🔊 Recorded audio saved at:", audio_file)

    text_output = transcribe_audio(audio_file)  # Convert speech to text
    print("\n📝 Transcribed Text:\n", text_output)

if __name__ == "__main__":
    main()
