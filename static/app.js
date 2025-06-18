// === Sound Effects ===
const moveSound = new Audio("/static/move.mp3");
const winSound = new Audio("/static/win.mp3");
let currentMode = "human";

// === Start from Mode Picker ===
function startSelectedMode() {
  const mode = document.getElementById("mode-select").value;
  currentMode = mode;
  startGame(mode);
}

// === Start Game with Mode and Random Starter ===
function startGame(mode) {
  fetch("/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mode, starter: null }) // random starter
  })
  .then(res => res.json())
  .then(state => {
    document.getElementById("mode-selection").style.display = "none";
    document.getElementById("game-section").style.display = "flex";
    updateStatus(state);
  });
}

// === Make Move ===
function makeMove(row, col) {
  moveSound.currentTime = 0;
  moveSound.play();

  fetch("/move", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ row, col }),
  })
  .then(res => res.json())
  .then(state => {
    updateStatus(state);
    if (state.winner) {
      winSound.currentTime = 0;
      winSound.play();
      launchConfetti();
    }
  });
}

// === Reset Board Only (Same Mode) ===
function resetGame() {
  fetch("/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mode: currentMode, starter: null })
  })
  .then(res => res.json())
  .then(state => {
    updateStatus(state);
  });
}

// === Back to Mode Selection ===
function goToModeSelect() {
  fetch("/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mode: "human", starter: null })
  }).then(() => {
    document.getElementById("game-section").style.display = "none";
    document.getElementById("mode-selection").style.display = "block";
  });
}

// === Draw Board ===
function createBoardUI(board, winningCells = []) {
  const boardDiv = document.getElementById("board");
  boardDiv.innerHTML = "";

  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      const cell = board[r][c];
      const cellDiv = document.createElement("div");
      cellDiv.classList.add("cell");
      if (cell === "X") cellDiv.classList.add("x");
      if (cell === "O") cellDiv.classList.add("o");
      if (winningCells.some(([wr, wc]) => wr === r && wc === c)) {
        cellDiv.classList.add("winner-cell");
      }
      cellDiv.textContent = cell;
      cellDiv.onclick = () => makeMove(r, c);
      boardDiv.appendChild(cellDiv);
    }
  }
}

// === Update UI with Game State ===
function updateStatus(state) {
  const status = document.getElementById("status");
  if (state.winner) {
    status.innerHTML = `🎉 <span style="color:${
      state.winner === "X" ? "#2980b9" : "#e74c3c"
    }">Player ${state.winner}</span> wins! 🎉`;
  } else {
    const phase = state.phase === 1 ? "Placement" : "Fade-and-Replace";
    status.innerHTML = `🎯 Player <span style="color:${
      state.current_player === "X" ? "#2980b9" : "#e74c3c"
    }">${state.current_player}</span>'s turn (${phase})`;
  }
  createBoardUI(state.board, state.winning_cells);
}

// === Theme Toggle ===
function toggleMode() {
  const body = document.body;
  body.classList.toggle("dark-mode");
  const btn = document.getElementById("mode-toggle");
  btn.textContent = body.classList.contains("dark-mode")
    ? "☀️ Light Mode"
    : "🌙 Dark Mode";
}

// === Confetti Animation ===
function launchConfetti() {
  confetti({ particleCount: 180, spread: 120, origin: { x: 0.5, y: 0.5 } });
}

// === Page Navigation ===
function showGame() {
  document.getElementById("game-section").style.display = "flex";
  document.getElementById("rules-section").style.display = "none";
  document.getElementById("about-section").style.display = "none";
}

function showRules() {
  document.getElementById("game-section").style.display = "none";
  document.getElementById("rules-section").style.display = "flex";
  document.getElementById("about-section").style.display = "none";
}

function showAbout() {
  document.getElementById("game-section").style.display = "none";
  document.getElementById("rules-section").style.display = "none";
  document.getElementById("about-section").style.display = "flex";
}
