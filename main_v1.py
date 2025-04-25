# main.py
# Spelling Bee Buddy
# Author: Moko Djane
# Created: April 2025

import tkinter as tk
import json
import datetime
import pyttsx3
import random
import os

def load_words(level="easy"):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "words.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(level, [])

def save_score(name, score, total):
    with open("scores.txt", "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time}, {name}, {score}/{total}\n")

def speak_word(word):
    engine = pyttsx3.init("nsss")  # macOS TTS engine
    engine.say(word)
    engine.runAndWait()

class SpellingBeeBuddy:
    def __init__(self, master):
        self.master = master
        master.title("Spelling Bee Buddy")

        self.score = 0
        self.total = 0
        self.time_left = 10
        self.current_word = ""
        self.words = []

        self.level_var = tk.StringVar(value="easy")
        self.name_var = tk.StringVar()

        self.setup_start_screen()

    def setup_start_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Enter your name:").pack()
        tk.Entry(self.master, textvariable=self.name_var).pack()

        tk.Label(self.master, text="Select difficulty:").pack()
        for level in ["easy", "medium", "hard"]:
            tk.Radiobutton(self.master, text=level.capitalize(), variable=self.level_var, value=level).pack()

        tk.Button(self.master, text="Start Game", command=self.start_game).pack()

    def start_game(self):
        self.name = self.name_var.get()
        self.words = load_words(self.level_var.get())
        self.score = 0
        self.total = 0
        self.next_word()

    def next_word(self):
        if not self.words:
            self.end_game()
            return

        self.current_word = random.choice(self.words)
        self.words.remove(self.current_word)
        self.time_left = 10

        self.show_game_screen()
        speak_word(self.current_word)
        self.update_timer()

    def show_game_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.timer_label = tk.Label(self.master, text=f"Time left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.pack()

        tk.Label(self.master, text=f"Spell the word: {self.current_word}", font=("Arial", 18)).pack()

        self.entry = tk.Entry(self.master, font=("Arial", 14))
        self.entry.pack()
        self.entry.focus()

        tk.Button(self.master, text="Submit", command=self.check_answer).pack()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.check_answer(timeout=True)

    def check_answer(self, timeout=False):
        user_input = self.entry.get().strip().lower()
        correct = self.current_word.lower()
        if not timeout and user_input == correct:
            self.score += 1
        self.total += 1
        self.next_word()

    def end_game(self):
        save_score(self.name, self.score, self.total)
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text=f"Game Over!\nScore: {self.score}/{self.total}", font=("Arial", 16)).pack()
        tk.Button(self.master, text="Play Again", command=self.setup_start_screen).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeBuddy(root)
    root.mainloop()