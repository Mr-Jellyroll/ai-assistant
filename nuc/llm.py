import requests

LLAMA_SERVER_URL = "http://localhost:8080/completion"

class AIModel:
    def __init__(self):
        """Initialize AI Model to use Llama.cpp server."""
        print("Using Llama.cpp server at:", LLAMA_SERVER_URL)

    def generate_response(self, transcript):
        """Send a request to the Llama.cpp server instead of running CLI."""
        payload = {
            "prompt": f"Question: '{transcript}'\nAnswer:",
            "n_predict": 150,  # Shorter responses improve speed
            "temperature": 0.7,  # Balanced creativity vs. deterministic output
            "top_k": 40,  # Limits sampling to top 40 tokens for efficiency
            "top_p": 0.8,  # Avoids unnecessary token sampling
            "repeat_penalty": 1.1,  # Reduces repeated phrases
            "threads": 8,  # Utilize more CPU cores
            "batch_size": 512  # Process more tokens at once
        }


        try:
            print(f"Sending request to Llama server: {LLAMA_SERVER_URL}")
            response = requests.post(LLAMA_SERVER_URL, json=payload)
            print(f"Llama Server Response Code: {response.status_code}")
            print(f"Llama Server Raw Response: {response.text}")

            if response.status_code == 200:
                response_data = response.json()
                ai_response = response_data.get("content", "").strip()  # Extract "content"
                print(f"Extracted AI Response: {ai_response}")  # Debugging print

                return ai_response if ai_response else "Error: No AI response generated"
            else:
                return f"Error: {response.text}"

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Llama server: {e}")
            return "Error: Llama server unavailable"
