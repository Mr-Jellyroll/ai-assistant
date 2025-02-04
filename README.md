

## Overview
The AI Assistant is a real-time system that:
- Listens to speech using WebRTC VAD.
- Transcribes speech to text using OpenAI Whisper.
- Generates AI-driven responses using Llama.cpp with Mistral 7B.
- Displays results in a GUI for real-time interaction.

## System Architecture
Project consists of two main components:

### **Local Machine**
- Captures live audio from the microphone.
- Uses VAD to detect when speech begins and ends.
- Sends audio data to the NUC for processing.
- Displays real-time transcriptions and AI-generated responses in a GUI.

### **NUC Server (Linux)**
- Processes audio using OpenAI Whisper for speech-to-text transcription.
- Generates responses using Llama.cpp with Mistral 7B.
- Provides an API backend for real-time interactions.

---

## Features
- **Live Audio Processing** – Captures audio with WebRTC VAD
- **Speech-to-Text** – Uses OpenAI **Whisper (base model)**
- **AI Response Generation** – Powered by **Llama.cpp with Mistral 7B**
- **Real-Time GUI & FastAPI Server** – Displays transcriptions & AI-generated responses
- **Optimized for Low Latency** – Uses **quantized GGUF models (Q4_K_M)** for speed

## LLM & NLP Technologies Used
- Whisper (Speech-to-Text) Model: Whisper Base
*Use Case: Converts spoken language into text with high accuracy.*
*Performance: Optimized for CPU inference.*

- Llama.cpp (LLM Inference) Model: Mistral 7B (Q4_K_M)
*Use Case: AI-powered interview answer generation.*
*Performance: Optimized quantized GGUF models for fast CPU-based inference.*

- WebRTC VAD (Voice Activity Detection)
*Use Case: Determines when speech starts and stops.*
*Performance: Filters out background noise & silent gaps.*

---


