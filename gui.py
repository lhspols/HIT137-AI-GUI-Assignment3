import tkinter as tk
from tkinter import scrolledtext
from models import TTSModel, SummarizerModel

OOP_EXPLANATION = """OOP Concepts Used:

1. Inheritance:
   - SummarizerModel and TTSModel extend the abstract class AIModel.
   - Both classes thus provide the 'run' method.

2. Polymorphism:
   - Both SummarizerModel and TTSModel have a 'run' method with different behavior.
   - The GUI can call 'run' on any object of class AIModel without knowing its type.

3. Encapsulation:
- Every model maintains its internal objects (pyttsx3 engine, summarizer pipeline) in its private.

4. Method Overriding:
   - 'run' method of every subclass overrides AIModel's abstract 'run' method.

5. Decorators:
   - 'timing_decorator' wraps the 'run' method to track execution time without changing the method itself.
"""

class AI_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI GUI Example")

        self.tts_model = TTSModel()
        self.summarizer_model = SummarizerModel()

        tk.Label(root, text="Enter Text:").pack()
        self.input_box = scrolledtext.ScrolledText(root, height=10, width=50)
        self.input_box.pack()

        tk.Button(root, text="Speak", command=self.speak_text).pack(pady=5)
        tk.Button(root, text="Summarize", command=self.summarize_text).pack(pady=5)

        tk.Label(root, text="Output:").pack()
        self.output_box = scrolledtext.ScrolledText(root, height=5, width=50)
        self.output_box.pack()

        tk.Label(root, text="OOP Explanation:").pack()
        self.oop_box = scrolledtext.ScrolledText(root, height=10, width=50)
        self.oop_box.pack()
        self.oop_box.insert(tk.END, OOP_EXPLANATION)
        self.oop_box.config(state=tk.DISABLED)

    def speak_text(self):
        text = self.input_box.get("1.0", tk.END).strip()
        self.tts_model.run(text)

    def summarize_text(self):
        text = self.input_box.get("1.0", tk.END).strip()
        summary = self.summarizer_model.run(text)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, summary)
