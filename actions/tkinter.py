import tkinter as tk
from tkinter import scrolledtext, Frame, Label, Entry, Button
import requests
from threading import Thread
import queue

class ChatBubble:
    def __init__(self, master, text="", sender="You"):
        self.master = master
        self.frame = Frame(master)
        self.sender = sender
        self.text = text
        self.bubble = Label(self.frame, text=self.text, wraplength=200,
                            bg="#DCF8C6" if sender == "You" else "#ECE5DD",
                            font=("Helvetica", 10), bd=2, justify="left", relief="groove", padx=5, pady=5)
        self.bubble.pack(padx=10, pady=5, anchor="e" if sender == "You" else "w")
        self.frame.pack(fill="both")

class RasaChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Selection Chatbot")
        self.message_queue = queue.Queue()
        self.create_widgets()
        self.process_responses()

    def create_widgets(self):
        # Frame for chat bubbles
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Entry widget for user input
        self.user_input = Entry(self.root, font=("Helvetica", 14))
        self.user_input.pack(fill="x", padx=10, pady=10)

        # Send button
        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            ChatBubble(self.frame, text=user_message, sender="You")
            self.user_input.delete(0, tk.END)
            thread = Thread(target=self.post_message_to_rasa, args=(user_message,))
            thread.start()

    def post_message_to_rasa(self, message):
        url = 'http://localhost:5005/webhooks/rest/webhook'
        payload = {"sender": "user", "message": message}
        try:
            response = requests.post(url, json=payload).json()
            self.message_queue.put(response)
        except Exception as e:
            self.message_queue.put([{"text": str(e)}])

    def process_responses(self):
        try:
            while not self.message_queue.empty():
                response = self.message_queue.get_nowait()
                for message in response:
                    if 'text' in message:
                        ChatBubble(self.frame, text=message['text'], sender="Mercedes AI")  # Change sender name here
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.process_responses)

def main():
    root = tk.Tk()
    app = RasaChatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()



