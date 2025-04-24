# Spelling Bee Buddy – Project Roadmap

## Sprint 1 – Initial Setup and Exploration

### ✅ Task 1: Search for related repositories on GitHub and evaluate their features.
- **Assigned to:** Moko  
- **Details:** Explored the [open-spelling-bee](https://github.com/philshem/open-spelling-bee) repository. Analyzed its use of a JSON word list and command-line interface. Found it effective for backend logic but limited in user engagement for kids.

### ✅ Task 2: Clone and test one repository.
- **Assigned to:** Moko  
- **Details:** Cloned and tested the "open-spelling-bee" repo. Verified its structure, ran the game, and noted its setup requirements. Identified areas to improve for GUI and interaction in Spelling Bee Buddy.

### ✅ Task 3: Create initial project structure in a new GitHub repository.
- **Assigned to:** Moko  
- **Details:** Initialized a new GitHub repo for Spelling Bee Buddy. Created folders for `assets`, `wordlists`, and `docs`. Added a basic Python file for game logic.

### ✅ Task 4: Implement a basic word display and input feature.
- **Assigned to:** Moko  
- **Details:** Developed a simple tkinter interface where players can see a word prompt and input their spelling. Added basic logic to check if the word is spelled correctly.

### ✅ Task 5: Document project setup and usage in the README.
- **Assigned to:** Moko  
- **Details:** Completed a `README.md` file outlining the project description, features, requirements, and setup instructions.

---

## Sprint 2 – Feature Development and Version Control

### ✅ Completed Tasks (6 significant commits)
- [x] Created basic tkinter interface with word prompt, input box, and feedback label.  
  _Commit:_ Set up basic tkinter interface with word display, input box, and feedback label for checking spelling

- [x] Added score tracking and automatic word progression after correct or incorrect answers.  
  _Commit:_ Added score tracking and automatic word progression after each attempt, to enhance gameplay flow

- [x] Connected word list to external JSON file for easier updates and level management.  
  _Commit:_ Connected word list to external JSON file for easier editing and scalability across difficulty levels

- [x] Added reset button to allow restarting the game without closing the window.  
  _Commit:_ Added reset button to allow users to restart the game after completion without closing the window

- [x] Implemented difficulty level selection (easy/medium/hard) via radio buttons.  
  _Commit:_ Added difficulty selection using radio buttons to allow users to choose between easy, medium, and hard word levels before starting

- [x] Implemented hint system that shows the first letter of a word on first incorrect attempt.  
  _Commit:_ Implemented hint system that displays the first letter of the word after an incorrect spelling attempt to support learning

---

## 🔧 In Progress / Future Enhancements
- [ ] Add pronunciation using text-to-speech (`pyttsx3` or `gTTS`)
- [ ] Create player name input and save scores per session
- [ ] Add timer or challenge mode for advanced practice

## 🌟 Stretch Ideas
- [ ] Multiplayer support or leaderboard
- [ ] Export score history to a file
- [ ] Add themed visuals or animation for younger users
