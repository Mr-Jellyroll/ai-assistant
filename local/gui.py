import tkinter as tk
import threading
import requests
import os
import time

NUC_API_URL = "http://192.168.1.3:8000/transcribe/"  # Update with your NUC IP

class AIInterviewAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Interview Assistant")
        self.root.geometry("800x600")  # Set window size (width x height)
        self.root.minsize(800, 600)  # Prevent resizing smaller than this


        # Transcription Label
        self.transcription_label = tk.Label(root, text="Transcription:", font=("Arial", 14, "bold"))
        self.transcription_label.pack(anchor="w", padx=10, pady=5)

        # Transcription Text
        self.transcription_text = tk.Text(root, height=15, width=80, wrap="word", font=("Arial", 12))
        self.transcription_text.pack(padx=10, pady=5)

        # AI Response Label
        self.response_label = tk.Label(root, text="AI Response:", font=("Arial", 14, "bold"))
        self.response_label.pack(anchor="w", padx=10, pady=5)

        # AI Response Text
        self.response_text = tk.Text(root, height=15, width=80, wrap="word", font=("Arial", 12))
        self.response_text.pack(padx=10, pady=5)

        # Record Button
        self.record_button = tk.Button(
            root, text="Start Recording", command=self.start_recording, font=("Arial", 14, "bold"),
            bg="#4CAF50",  # Green background
            fg="black",  
            activebackground="#45a049",  # Darker green when clicked
            activeforeground="white",  # White text when clicked
            padx=20, pady=10,  
            borderwidth=3, relief="raised",  
            highlightbackground="black",  
            highlightthickness=2  # 
)
        self.record_button.pack(pady=20)  


    def start_recording(self):
        print("Start Recording button clicked!")  
        self.record_button.config(
            text="Recording...", state=tk.DISABLED,
            bg="#D32F2F",  # Red when recording
            activebackground="#B71C1C"  # Darker red on click
    )
        threading.Thread(target=self.process_audio).start() 


    def process_audio(self):
        """Records speech, sends it to the NUC, and updates the GUI with results."""
        print("Recording audio...")  

        # Step 1: Capture Audio
        os.system("python local/audio_capture.py")  # Run the recording script
        time.sleep(1)  # Small delay to ensure file is saved
        print("Audio recording completed!")  

        # Step 2: Send to NUC API
        file_path = "local/speech.wav"
        if not os.path.exists(file_path):
            print("Error: Speech file not found!")  
            return

        print("Sending audio to NUC...")
        with open(file_path, "rb") as audio_file:
            files = {"file": audio_file}
            response = requests.post(NUC_API_URL, files=files)

        if response.status_code == 200:
            data = response.json()
            transcription = data.get("transcription", "No transcription available")
            ai_response = data.get("ai_response", "No AI response generated")

            print(f"Received Transcription: {transcription}")  # Debugging
            print(f"Received AI Response: {ai_response}")  # Debugging

            self.transcription_text.delete("1.0", tk.END)
            self.transcription_text.insert(tk.END, transcription)

            self.response_text.delete("1.0", tk.END)
            self.response_text.insert(tk.END, ai_response)

        else:
            print(f"Error: No AI response received! Server response: {response.text}")



        # Reset Button
        self.record_button.config(text="Start Recording", state=tk.NORMAL, bg="green")


if __name__ == "__main__":
    root = tk.Tk()
    app = AIInterviewAssistant(root)
    root.mainloop()
