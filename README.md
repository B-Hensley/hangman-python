# Hangman Game 🕵️‍♂️🎩  

A simple text-based **Hangman** game in Python! This version of Hangman randomly selects an animal and challenges the player to guess the word before running out of attempts.  

## 🎮 How to Play  

1. Run the script using Python.  
2. Choose whether to play (`y` for yes, `n` for no).  
3. Guess letters one at a time.  
4. Each incorrect guess adds a body part to the Hangman.  
5. Guess the full word before the Hangman is complete to win!  

## 📜 Features  

✅ Random word selection from an `animals_list.py` file  
✅ Input validation for correct letter guesses  
✅ Tracks guessed letters to prevent duplicate inputs  
✅ ASCII Hangman visual updates for each wrong guess  
✅ Replay option after a game ends  

## 📂 File Structure  

```plaintext
📦 Hangman-Game
├── 📜 hangman.py          # Main game logic
├── 📜 animals_list.py     # List of words (animals)
├── 📜 hangman_stages.py   # ASCII art for Hangman stages
├── 📜 README.md           # Documentation
└── 📜 requirements.txt    # (Optional) Dependencies file
```

## 🛠️ Setup  

### 1. Clone the repository:  
  ```sh
  git clone https://github.com/yourusername/Hangman-Game.git
  ```
### 2. Navigate to the project directory:
  ```sh
  cd Hangman-Game
  ```
### 3. Run the game:
  ```sh
python hangman.py
  ```

## 📝 Notes
- Ensure animals_list.py contains a list variable named animals.
- The game requires Python 3.

### 💡 Created by **Brenda Hensley**
### 🐍 Built with Python
### 📌 Feel free to contribute or suggest improvements!
