from fastapi import FastAPI, File, UploadFile
import shutil
import sys
import os
sys.path.append(os.path.dirname(__file__))  # Ensure Python finds `nuc/`
from llm import AIModel
from transcription import Transcriber

app = FastAPI()
transcriber = Transcriber()
ai_model = AIModel()  # This line initializes the AI model


app = FastAPI()
transcriber = Transcriber()  # Load Whisper model once

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """Receives an audio file, transcribes it, and generates an AI response."""
    file_path = f"temp_{file.filename}"

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe the audio
    transcript = transcriber.transcribe_audio(file_path)
    print(f"Transcript: {transcript}")  # Debugging print

    # Generate AI response
    ai_response = ai_model.generate_response(transcript)
    print(f"AI Response: {ai_response}")  # Debugging print

    return {"transcription": transcript, "ai_response": ai_response}


@app.get("/")
def root():
    return {"message": "NUC Whisper API is running!"}
