var scoreTo = document.querySelector("#text");
var playerOne = document.querySelector("#player1");
var playerTwo = document.querySelector("#player2");
var reset = document.querySelector("#btn");
var playingTo = document.querySelector("#playing_to");
var scoreOne = document.querySelector("#scr1");
var scoreTwo = document.querySelector("#scr2");
var win = document.querySelector("#win");
var rtext = document.querySelector("#resettext");
var wrapper = document.querySelector("#wrapper");
var scr1 = 0;
var scr2 = 0;
var refreshId;
var bln = false;
var winningScore = 0;

scoreTo.addEventListener("keypress", function (event) {
    var key = event.which;
    if (key === 13) {
        playingTo.textContent = scoreTo.value;
        winningScore = Number(scoreTo.value);
        rst();
    }
});

playerOne.addEventListener("click", function () {
    if (!bln && winningScore > 0) {
        scr1++;
        scoreOne.textContent = scr1;
        winner();
    }
});

playerTwo.addEventListener("click", function () {
    if (!bln && winningScore > 0) {
        scr2++;
        scoreTwo.textContent = scr2;
        winner();
    }
});

function winner() {
    if ((scr1 === winningScore) || (scr2 === winningScore)) {
        win.textContent = ((scr1 === winningScore) ? "Player One Wins!!!" : "Player Two Wins!!!");
        refreshId = setInterval(backgound, 100);
    }
}

function rst() {
    clearInterval(refreshId);
    document.querySelector("#wrapper").style.backgroundColor = "white";
    scoreOne.textContent = 0;
    scoreTwo.textContent = 0;
    scr1 = 0;
    scr2 = 0;
    win.textContent = "";
    rtext.textContent = "";
    bln = false;
    scoreTo.value = null;
}

function backgound() {
    rtext.textContent = "Please reset the scoreboard!";
    bln = true;
    wrapper.style.backgroundColor =(wrapper.style.backgroundColor === "red") ? "green" : "red";
}

reset.addEventListener("click", rst);