var HOUR = 9;
var MINUTE = 50;
var PERIOD = "AM";
var time = HOUR.toString(HOUR);

if (MINUTE < 30){
    time ="It's just after " + HOUR.toString();
}

else if (MINUTE > 30){
    time ="It's almost " + (HOUR+1).toString();
}

else {
    time = "It's " + HOUR.toString() + " and a Half";

}
switch (PERIOD) {

    case "AM" :
        time += " in the morning";
        break;

    case "PM" :
        time += " in the evening";
        break;

}

console.log(time);