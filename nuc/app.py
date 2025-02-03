from fastapi import FastAPI, File, UploadFile
import shutil
from nuc.transcription import Transcriber

app = FastAPI()
transcriber = Transcriber()  # Load Whisper model once

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """Receives an audio file, saves it, and transcribes it using Whisper."""
    file_path = f"temp_{file.filename}"
    
    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe the audio
    text = transcriber.transcribe_audio(file_path)
    
    return {"transcription": text}

@app.get("/")
def root():
    return {"message": "NUC Whisper API is running!"}
