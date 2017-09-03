var easy = document.querySelector("#easy");
var hard = document.querySelector("#hard");
var playAgain = document.querySelector("#playagain");
var bln = false;
var correct = document.querySelector("#correct");
var win = document.querySelector("h2");
var square = document.querySelectorAll(".square");
var rgbColor = document.querySelector("h3");
var point = document.querySelector("#points");
var winningColor;
var playCount = 3;
var difficulty = 6;
var colors = [];
var won = false;
var count = 0;
var points = 0;

hard.classList.add("active");
colorChanger();

easy.addEventListener("click", function () {
    difficulty = 3;
    this.classList.add("active");
    hard.classList.remove("active");
    bln = false;
    colorChanger();
});

hard.addEventListener("click", function () {
    difficulty = 6;
    this.classList.add("active");
    easy.classList.remove("active");
    bln = true;
    colorChanger();
});

playAgain.addEventListener("click", function () {
    colorChanger();
});

function colorChanger() {
    won = false;
    count = 0;
    playAgain.textContent = "CHANGE COLORS?";
    correct.textContent = "";
    win.textContent = "Guest the correct rgb color";
    colorsGenerator();
    (difficulty === 3) ? hideSquares() : showSquares();
    playCount = (difficulty === 3) ? 2 : 3;
}

function colorsGenerator() {
    colors.length = difficulty;
    for (var i = 0; i < difficulty; i++) {
        var r = Math.floor(Math.random() * 256);
        var g = Math.floor(Math.random() * 256);
        var b = Math.floor(Math.random() * 256);
        colors[i] = ("rgb" + "(" + r + ", " + g + ", " + b + ")");
    }
    for (var j = 0; j < colors.length; j++) {
        square[j].style.backgroundColor = colors[j];
    }
    winningColor = colors[Math.floor(Math.random() * difficulty)];
    rgbColor.textContent = winningColor;
}

function hideSquares() {
    for (var l = 3; l < 6; l++) {
        square[l].style.display = "none";
    }
}

function showSquares() {
    for (var l = 3; l < 6; l++) {
        square[l].style.display = "inline-block";
    }
}

for (var e = 0; e < difficulty; e++) {
    square[e].addEventListener("click", clicked);
}

function clicked() {
    if (count < playCount && won === false) {
        if (this.style.backgroundColor === winningColor) {
            for (var k = 0; k < difficulty; k++) {
                square[k].style.backgroundColor = winningColor
            }
            win.textContent = "GOOD JOB!!!";
            correct.textContent = "Correct!";
            flash(10, "green");
            won = true;
            if (difficulty === 6) {
                switch (count) {
                    case 0:
                        points += 5;
                        break;
                    case 1:
                        points += 3;
                        break;
                    case 2:
                        points += 1;
                        break;
                    default:
                        points += 1;
                }
            }
            else {
                switch (count) {
                    case 0:
                        points += 2;
                        break;
                    case 1:
                        points += 1;
                        break;
                    default:
                        points += 1;
                }
            }
            playAgain.textContent = "PLAY AGAIN?";
            point.textContent = points;
        }
        else {
            count++;
            correct.textContent = "Wrong!";
            this.style.backgroundColor = "transparent";
            win.textContent = (count < playCount) ? count + "/" + playCount : "Game Over!";
            if (count >= playCount) {
                playAgain.textContent = "PLAY AGAIN?";
            }
            flash(6, "red");
        }
    }
}

function flash(x, w) {
    var flashCount = 0;
    var rid;
    correct.style.backgroundColor = w;
    rid = setInterval(function () {
        correct.classList.toggle(w);
        flashCount++;
        if (flashCount === x) {
            clearInterval(rid);
        }
    }, 100);
}