const moves = ["Rock", "Paper", "Scissors"];

function play(userChoice) {
    const pcChoice = Math.floor(Math.random() * 3);
    document.getElementById("choices").innerText =
    `You chose: ${moves[userChoice]} | PC chose: ${moves[pcChoice]}`;

    const winner = determineWinner(userChoice, pcChoice);

    document.getElementById("result").innerText = winner;

    // Mostrar botão reiniciar e esconder os botões de jogada
    document.getElementById("restart").style.display = "inline-block";
    Array.from(document.querySelectorAll("button")).forEach(btn => {
    if(btn.id !== "restart") btn.style.display = "none";
    });
}

function determineWinner(user, pc) {
    if(user === pc) return "Draw!";
    if (
    (pc === 2 && user === 1) ||
    (pc === 1 && user === 0) ||
    (pc === 0 && user === 2)
    ) {
    return "PC wins!";
    } else {
    return "You win!";
    }
}

function restart() {
    document.getElementById("choices").innerText = "";
    document.getElementById("result").innerText = "";
    document.getElementById("restart").style.display = "none";
    Array.from(document.querySelectorAll("button")).forEach(btn => btn.style.display = "inline-block");
}
