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


function updateStatus(state) {
  const statusDiv = document.getElementById("status");
  if (state.winner) {
    statusDiv.innerHTML = `🎉 <span style="color:${
      state.winner === "X" ? "#2980b9" : "#e74c3c"
    }">Player ${state.winner}</span> wins! 🎉`;
    launchConfetti();
  } else {
    const phase = state.phase === 1 ? "Placement" : "Fade-and-Replace";
    statusDiv.innerHTML = `🎯 Player <span style="color:${
      state.current_player === "X" ? "#2980b9" : "#e74c3c"
    }">${state.current_player}</span>'s turn (${phase})`;
  }

  createBoardUI(state.board, state.winning_cells);
}

function launchConfetti() {
  // Central celebration burst
  confetti({
    particleCount: 200,
    spread: 140,
    startVelocity: 45,
    origin: { x: 0.5, y: 0.5 },
    gravity: 0.6,
    scalar: 1.2,
    colors: ['#00f0ff', '#ff4f81', '#ffcc00', '#7d5fff', '#2ed573']
  });

  // Small side bursts for extra joy
  setTimeout(() => {
    confetti({
      particleCount: 60,
      angle: 60,
      spread: 100,
      origin: { x: 0, y: 0.5 },
      scalar: 1.1,
      colors: ['#ff4f81', '#ffeaa7']
    });
    confetti({
      particleCount: 60,
      angle: 120,
      spread: 100,
      origin: { x: 1, y: 0.5 },
      scalar: 1.1,
      colors: ['#7d5fff', '#00f0ff']
    });
  }, 250);
}





function resetGame() {
  fetch("/reset", { method: "POST" })
    .then((res) => res.json())
    .then((state) => {
      updateStatus(state);
    });
}

window.onload = resetGame;

function toggleMode() {
  const body = document.body;
  body.classList.toggle("dark-mode");

  const modeButton = document.getElementById("mode-toggle");
  if (body.classList.contains("dark-mode")) {
    modeButton.textContent = "☀️ Light Mode";
  } else {
    modeButton.textContent = "🌙 Dark Mode";
  }
}


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

const moveSound = new Audio('/static/move.mp3');
const winSound  = new Audio('/static/win.mp3');

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


