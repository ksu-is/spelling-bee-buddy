
# 🐝 Spelling Bee Buddy

Spelling Bee Buddy is an educational game designed to help kids practice and improve their spelling skills in a fun, interactive way! Built using Python and tkinter, the game integrates text-to-speech pronunciation, a countdown timer for each word, background music, and score saving.

---

## 🎮 Features

- **Text-to-Speech (TTS):** Each word is pronounced using pyttsx3 to assist auditory learners.
- **Countdown Timer:** Players have 10 seconds to spell each word, adding challenge and excitement.
- **Difficulty Levels:** Easy, Medium, and Hard word lists to match player skill levels.
- **Name Entry and Score Saving:** Player names and scores are saved automatically in a `scores.txt` file.
- **Background Music:** Looped theme music during gameplay for a fun atmosphere.
- **Dynamic Sound Balancing:** Music volume lowers when a word is pronounced for clarity.
- **User-Friendly Interface:** Easy navigation between start screen, game play, and final score screens.

---

## 🛠️ How to Run

1. Install required packages:
   ```bash
   pip install pyttsx3 pygame
   ```

2. Ensure you have the following files in the same directory:
   - `main_v1.py` (or updated version)
   - `words.json` (word bank by difficulty)
   - `theme.mp3` (background music)
   - `scores.txt` (will auto-create if missing)

3. Run the game:
   ```bash
   python main_v1.py
   ```

---

## 📁 Project Structure

```
/spelling-bee-buddy/
│
├── main_v1.py
├── words.json
├── theme.mp3
├── scores.txt
├── README.md
├── projectroadmap.md
```

---

## ✏️ Acknowledgments

- Open-source references: *open-spelling-bee* repository.
- Sound effects and music: Royalty-free tracks from Pixabay.
- Built as part of Sprint 1, 2, and 3 for educational project development.