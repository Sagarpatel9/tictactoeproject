#  FadeTacToe: A Strategic Variant of Tic-Tac-Toe

Welcome to a unique twist on the classic Tic Tac Toe!  
This project reimagines the traditional game by adding a strategic second phase where players must **fade out** old pieces to make room for new ones — eliminating the repetitive, draw-prone gameplay of the original.

---

## 🧠 Game Features

- **Two Phases of Play:**
  1. **Placement Phase** – Players alternate turns to place up to 3 pieces.
  2. **Fade-and-Replace Phase** – Players replace their oldest piece with a new move.

- **Game Modes:**
  - Human vs Human
  - Human vs AI (with Alpha-Beta Pruning)

- **Smart Visual Cues:**
  - Glowing oldest pieces during fade-and-replace phase
  - Confetti and sound effects on win
  - Light/Dark theme toggle

---

## 🗂️ Layout of the Code

A quick breakdown to help other CS students understand the structure:

### 🔧 Backend

- `app.py` – Flask application that connects front-end and game logic
- `game.py` – Game engine managing rules, moves, and win logic
- `ai_agent.py` – AI logic using Minimax with Alpha-Beta pruning

### 🎨 Frontend

- `templates/index.html` – HTML layout with game board and UI buttons
- `static/style.css` – CSS styling for the board, animations, and themes
- `static/app.js` – JavaScript handling game interaction, sound, effects

### 🔊 Assets

- `static/move.mp3` – Sound for a player move
- `static/win.mp3` – Sound for a win animation

### 📦 Other

- `requirements.txt` – Python dependencies for running the Flask app
- `README.md` – Documentation for understanding and running the project

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Sagarpatel9/tictactoeproject.git
cd tictactoeproject
```

### 2. Set up a virtual enviroment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Start the Server
```bash
python app.py
```

### 5. Play the game 
User should see something like:
```bash
http://localhost:5000
```

### Credit:

Team Members: Sagar Patel, Simegnew Bayu

AI: Implemented using Alpha-Beta Pruning

Frameworks/Libraries: Flask, Vanilla JS/CSS, Confetti.js

Assisted by: ChatGPT (OpenAI) for development guidance and documentation




