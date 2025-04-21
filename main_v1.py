# main.py
# Spelling Bee Buddy - Version 5
# Author: Moko Djane
# Created: April 2025

import tkinter as tk
import json

def load_words(level="easy"):
    with open("words.json", "r") as f:
        data = json.load(f)
    return data.get(level, [])

class SpellingBeeBuddy:
    def __init__(self, master):
        self.master = master
        self.master.title("Spelling Bee Buddy")
        self.level_var = tk.StringVar(value="easy")
        
        # Difficulty selection
        tk.Label(master, text="Select difficulty:").pack()
        for lvl in ["easy", "medium", "hard"]:
            tk.Radiobutton(master, text=lvl.title(), variable=self.level_var, value=lvl).pack(anchor="w")
        
        tk.Button(master, text="Start Game", command=self.start_game).pack(pady=5)

        self.word_label = tk.Label(master, text="")
        self.word_label.pack()

        self.entry = tk.Entry(master, state="disabled")
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_spelling, state="disabled")
        self.submit_button.pack()

        self.feedback = tk.Label(master, text="")
        self.feedback.pack()

        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game, state="disabled")
        self.reset_button.pack()

    def start_game(self):
        self.level = self.level_var.get()
        self.words = load_words(self.level)
        self.current_index = 0
        self.score = 0

        if self.words:
            self.word_label.config(text=self.words[self.current_index])
        else:
            self.word_label.config(text="No words found.")

        self.entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.feedback.config(text="")
        self.reset_button.config(state="disabled")

    def check_spelling(self):
        user_input = self.entry.get().strip().lower()
        correct_word = self.words[self.current_index]

        if user_input == correct_word:
            self.score += 1
            self.feedback.config(text=f"Correct! Score: {self.score}")
        else:
            self.feedback.config(text=f"Incorrect! The word was {correct_word}")

        self.entry.delete(0, tk.END)
        self.current_index += 1
        if self.current_index < len(self.words):
            self.word_label.config(text=self.words[self.current_index])
        else:
            self.word_label.config(text="Game Over")
            self.entry.config(state="disabled")
            self.submit_button.config(state="disabled")
            self.reset_button.config(state="normal")
            self.feedback.config(text=f"Final score: {self.score}/{len(self.words)}")

    def reset_game(self):
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeBuddy(root)
    root.mainloop()