from app.audio_processing import record_audio
from app.speech_to_text import transcribe_audio
import time
from app.questions import QUESTIONS
from app.intent_detection import detect_intent
from app.router import route_intent
from app.router import ExitIntent


def main():
    
    print("🎙 Starting real-time will generation...")
    question_index = 0

    try:
        while question_index < len(QUESTIONS):
            print(f"\n❓ Question {question_index + 1}: {QUESTIONS[question_index]}")
            ready = input("🎤 Are you ready to answer? (Press 'Y' to record): ").strip().lower()
            # ready = input("🎤 Are you ready to answer? (Press 'Y' to record, 'N' to skip): ").strip().lower()
            # if ready != 'y':
            #     print("⏭️ Skipping this question.")
            #     question_index += 1
            #     continue
            while True:  # Ensures we handle blank responses properly


                audio_file = record_audio()
                print("🔊 Recorded audio saved at:", audio_file)

                transcribed_text = transcribe_audio(audio_file)
                print("\n📝 Transcribed Text:", transcribed_text)

                if transcribed_text:  # If valid audio input is received, process intent
                    intent = detect_intent(transcribed_text)

                    if intent == "repeat":
                            print(f"\n❓ Question {question_index + 1}: {QUESTIONS[question_index]}")
                            # print("⏭️ Skipping this question.")
                            continue  # Move to the same question
                    
                    action_response = route_intent(intent)
                    print("🤖 AI Response:", action_response)
                    break  # Valid response received, exit internal loop

                else:  # Handle case where no response is detected
                    print("⚠️ You did not respond. Do you want to (skip, repeat, or exit)?")
                    ready = input("🎤 Are you ready to answer? (Press 'Y' to record): ").strip().lower()
                #     audio_file = record_audio()
                #     transcribed_text = transcribe_audio(audio_file)
                #     intent = detect_intent(transcribed_text)

                # # if intent == "skip":
                # #     break  # Move to the next question

                #     action_response = route_intent(intent)
                #     print("🤖 AI Response:", action_response)

            question_index += 1    
            
    except ExitIntent:
        print("👋 Exiting the process. Goodbye!")

    
    print("✅ Will generation process completed!")

        

    # audio_file = record_audio()  # Record until silence is detected
    # print("🔊 Recorded audio saved at:", audio_file)

    # text_output = transcribe_audio(audio_file)  # Convert speech to text
    # print("\n📝 Transcribed Text:\n", text_output)

if __name__ == "__main__":
    main()
