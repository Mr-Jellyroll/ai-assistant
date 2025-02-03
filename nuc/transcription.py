import whisper

class Transcriber:
    def __init__(self, model_size="base"):
        """
        Initialize Whisper model on the NUC.
        'base' is a good balance of speed & accuracy.
        """
        print(f"Loading Whisper model: {model_size}...")
        self.model = whisper.load_model(model_size)

    def transcribe_audio(self, audio_path):
        """Transcribe speech from an audio file."""
        print(f"Transcribing {audio_path}...")
        result = self.model.transcribe(audio_path)
        return result["text"]

if __name__ == "__main__":
    transcriber = Transcriber()
    transcript = transcriber.transcribe_audio("speech.wav")
    print("\nTranscription:\n", transcript)
