import tkinter as tk
from tkinter import scrolledtext
from models import SummarizerModel
import pyttsx3

class AI_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI GUI Example")
        self.summarizer_model = SummarizerModel()
        tk.Label(root, text="Enter Text:").pack()
        self.input_box = scrolledtext.ScrolledText(root, height=10, width=50)
        self.input_box.pack()
        tk.Button(root, text="Speak", command=self.speak_text).pack(pady=5)
        tk.Button(root, text="Summarize", command=self.summarize_text).pack(pady=5)
        tk.Label(root, text="Output:").pack()
        self.output_box = scrolledtext.ScrolledText(root, height=5, width=50)
        self.output_box.pack()

    def speak_text(self):
        text = self.input_box.get("1.0", tk.END).strip()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def summarize_text(self):
        text = self.input_box.get("1.0", tk.END).strip()
        summary = self.summarizer_model.run(text)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, summary)

if __name__ == "__main__":
    root = tk.Tk()
    gui = AI_GUI(root)
    root.mainloop()

