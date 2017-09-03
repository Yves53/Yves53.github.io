var daysUntilMyBirthday = 60;
while (daysUntilMyBirthday >= 0 ){
    if (daysUntilMyBirthday === 0){console.log("IT'S MY BIRTHDAY!")}
    else if (daysUntilMyBirthday > 5){console.log(daysUntilMyBirthday + " days until my birthday." + ((daysUntilMyBirthday >= 30) ? "Such a long time... :(" : "I'm excited :)"));}
    else {(console.log(daysUntilMyBirthday + ((daysUntilMyBirthday > 1) ? " days until my birthday. I'm so excited.".toUpperCase() : " day until my birthday. I can taste it.".toUpperCase())));}
    daysUntilMyBirthday--;
}