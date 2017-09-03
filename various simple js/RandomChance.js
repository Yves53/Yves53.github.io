function randomChance(a) {
    var winningNumber = Math.floor(Math.random() * 100) + 1;
    var coins = a;
    for (var i = 1; i <= a; i++) {

        var number = Math.floor(Math.random() * 100) + 1;
        coins--;
        if (number === winningNumber) {

            coins += (Math.floor(Math.random() * 100) + 50);

            console.log("CONGRATULATIONS!!!, you won.")
            break;
        }
    }

    if (coins === 0) {
        console.log("You lost all you coins!")
    }

    console.log("The number of quarters you have is " + coins);
}

randomChance(60);