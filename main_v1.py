# main.py
# Spelling Bee Buddy - Version 1
# Author: Moko Djane
# Created: April 2025

import tkinter as tk

def load_words():
    return ["apple", "banana", "grape"]

class SpellingBeeBuddy:
    def __init__(self, master):
        self.master = master
        self.master.title("Spelling Bee Buddy")
        self.words = load_words()
        self.current_index = 0

        self.word_label = tk.Label(master, text=self.words[self.current_index])
        self.word_label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_spelling)
        self.submit_button.pack()

        self.feedback = tk.Label(master, text="")
        self.feedback.pack()

    def check_spelling(self):
        user_input = self.entry.get().strip().lower()
        correct_word = self.words[self.current_index]

        if user_input == correct_word:
            self.feedback.config(text="Correct!")
        else:
            self.feedback.config(text="Incorrect!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingBeeBuddy(root)
    root.mainloop()
