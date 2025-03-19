import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import wave
import time


def is_speech(audio_chunk, silence_thresh=-40):
    """
    Detects speech by checking if the audio chunk is above a silence threshold.
    :param audio_chunk: Numpy array of recorded audio.
    :param silence_thresh: Silence threshold in dB.
    :return: True if speech is detected, False if silent.
    """
    audio_segment = AudioSegment(
    audio_chunk.tobytes() if isinstance(audio_chunk, np.ndarray) else audio_chunk,
    frame_rate=16000,
    sample_width=2,
    channels=1
)
    nonsilent_ranges = detect_nonsilent(audio_segment, min_silence_len=700, silence_thresh=silence_thresh)
    return len(nonsilent_ranges) > 0    # True if speech is detected        

def record_audio(filename="samples/user_speech.wav", pause_duration=2, silence_threshold=-40):
    """
    Records audio in real-time and stops when silence is detected for a longer duration.
    :param filename: Path to save recorded audio.
    :param duration: Time in seconds to wait for silence before stopping.
    :param silence_threshold: dB threshold for silence detection.
    :return: Saved audio filename.
    """
    sample_rate = 16000
    channels = 1
    dtype = np.int16
    buffer_duration = 0.5  # Process audio in 0.5 sec chunks
    silence_count = 0
    max_silence_chunks = int(pause_duration / buffer_duration)
    silence_start_time = None
    print("🎤 Speak now... Recording will stop when you finish talking.")

    with sd.InputStream(samplerate=sample_rate, channels=channels, dtype=dtype) as stream:
        audio_frames = []
        start_time = time.time()
        
        while True:
            data, _ = stream.read(int(sample_rate * buffer_duration))
            audio_frames.append(data)

            # Convert full audio into a single byte array
            full_audio = b"".join(audio_frames)

            # # Check if speech is detected
            audio_np = np.frombuffer(full_audio[-int(sample_rate * pause_duration * 2):], dtype=np.int16)

            if is_speech(audio_np, silence_threshold):
                # Reset silence count and silence timer
                if silence_start_time is not None:
                    silence_duration = time.time() - silence_start_time
                    print(f"🔊 Speech detected after {silence_duration:.2f} seconds of silence.")
                    silence_start_time = None  # Reset timer
                silence_count = 0  # Reset silence count
            
            else:
                if silence_start_time is None:
                    silence_start_time = time.time()
                silence_count += 1  # Increment silent count

            
            if silence_count >= max_silence_chunks:
                # silence_duration = time.time() - silence_start_time if silence_start_time else 0
                total_silence_duration = time.time() - silence_start_time
                print(f"🛑 Silence detected for {total_silence_duration:.2f} seconds. Stopping recording.")
                break

        print(f"⏳ Recording duration: {time.time() - start_time:.2f} sec")

    # Save the recorded audio
    wave_file = wave.open(filename, "wb")
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b"".join(audio_frames))
    wave_file.close()

    return filename
