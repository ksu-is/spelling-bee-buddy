# main.py
# Spelling Bee Buddy
# Author: Moko Djane
# Created: April 2025

import tkinter as tk
import json
import datetime

def load_words(level="easy"):
    with open("words.json", "r") as f:
        data = json.load(f)
    return data.get(level, [])

def save_score(name, score, total):
    with open("scores.txt", "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time}, {name}, {score}/{total}\n")

class SpellingBeeBuddy:
    def __init__(self, master):
        self.master = master
        self.master.title("Spelling Bee Buddy")
        self.level_var = tk.StringVar(value="easy")
        self.name_var = tk.StringVar()

        # Welcome screen widgets
        self.intro_label = tk.Label(master, text="Welcome to Spelling Bee Buddy!", font=("Arial", 16))
        self.intro_label.pack(pady=10)

        tk.Label(master, text="Enter your name:").pack()
        self.name_entry = tk.Entry(master, textvariable=self.name_var)
        self.name_entry.pack(pady=5)

        tk.Label(master, text="Select difficulty:").pack()
        for lvl in ["easy", "medium", "hard"]:
            tk.Radiobutton(master, text=lvl.title(), variable=self.level_var, value=lvl).pack(anchor="w")

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        # Game widgets
        self.word_label = tk.Label(master, text="")
        self.entry = tk.Entry(master, state="disabled")
        self.submit_button = tk.Button(master, text="Submit", command=self.check_spelling, state="disabled")
        self.feedback = tk.Label(master, text="")
        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game, state="disabled")

    def start_game(self):
        self.name = self.name_var.get().strip()
        if not self.name:
            self.feedback.config(text="Please enter your name to start.")
            self.feedback.pack()
            return

        self.words = load_words(self.level_var.get())
        self.current_index = 0
        self.score = 0

        self.intro_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.feedback.pack_forget()

        self.word_label.config(text=self.words[self.current_index])
        self.word_label.pack()
        self.entry.config(state="normal")
        self.entry.pack()
        self.submit_button.config(state="normal")
        self.submit_button.pack()
        self.feedback.config(text="")
        self.feedback.pack()
        self.reset_button.pack()

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
            save_score(self.name, self.score, len(self.words))

    def reset_game(self):
        self.word_label.pack_forget()
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.feedback.pack_forget()
        self.reset_button.pack_forget()
        self.__init__(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeBuddy(root)
    root.mainloop()