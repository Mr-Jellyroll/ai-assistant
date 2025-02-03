import pyaudio
import webrtcvad
import wave
import time

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # Whisper performs best at 16kHz
FRAME_DURATION = 20  # Frame size: 10, 20, or 30 ms
FRAME_SIZE = int(RATE * (FRAME_DURATION / 1000))  # 320 samples for 20ms

VAD_MODE = 1  # Less aggressive VAD (0-3)
SILENCE_TOLERANCE = 2.0  # Wait 2 seconds of silence before stopping

class AudioCapture:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.vad = webrtcvad.Vad(VAD_MODE)

        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=FRAME_SIZE)

    def detect_speech(self, frame):
        """Check if the audio frame contains speech."""
        return self.vad.is_speech(frame, RATE)

    def record_audio(self, output_filename="speech.wav"):
        """Records audio while speech is detected, with a silence buffer."""
        frames = []
        silent_chunks = 0
        max_silent_chunks = int(SILENCE_TOLERANCE * (1000 / FRAME_DURATION))  # Convert sec to frames

        print("Listening for speech...")

        while True:
            audio_frame = self.stream.read(FRAME_SIZE, exception_on_overflow=False)
            if self.detect_speech(audio_frame):
                print("Speech detected! Recording...")
                frames.append(audio_frame)
                silent_chunks = 0  # Reset silence counter
            elif frames:
                silent_chunks += 1
                print(f"Silence detected ({silent_chunks}/{max_silent_chunks})")
                if silent_chunks >= max_silent_chunks:
                    print("Silence tolerance exceeded, stopping recording.")
                    break

        # Save the recorded speech
        with wave.open(output_filename, "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b"".join(frames))

        print(f"Audio saved as {output_filename}")

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    capture = AudioCapture()
    capture.record_audio()
    capture.close()
