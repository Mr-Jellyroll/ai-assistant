import subprocess
import os

MODEL_PATH = os.path.expanduser("~/ai-assistant/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")
LLAMA_CLI_PATH = os.path.expanduser("~/ai-assistant/llama.cpp/build/bin/llama-cli")

class AIModel:
    def __init__(self):
        """Initialize Llama.cpp with Mistral 7B."""
        if not os.path.exists(LLAMA_CLI_PATH):
            raise FileNotFoundError("Llama.cpp binary not found. Make sure you compiled it.")

    def generate_response(self, prompt):
        """Generate AI response using Llama.cpp."""
        command = [
            LLAMA_CLI_PATH,
            "-m", MODEL_PATH,
            "--prompt", prompt,
            "--n-predict", "200"
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()

if __name__ == "__main__":
    ai = AIModel()
    print(ai.generate_response("What team won the 1984 NBA championship and who was league MVP?"))
