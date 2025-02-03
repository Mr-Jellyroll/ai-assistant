import requests

NUC_API_URL = "http://192.168.1.3:8000/transcribe/"

def send_audio(file_path="speech.wav"):
    """Send audio to the NUC for transcription."""
    with open(file_path, "rb") as audio_file:
        files = {"file": audio_file}
        response = requests.post(NUC_API_URL, files=files)
    
    if response.status_code == 200:
        print("Transcription:", response.json()["transcription"])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    send_audio()
