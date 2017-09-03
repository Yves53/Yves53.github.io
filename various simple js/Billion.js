var money = 0.01;
var total = money;
for (var i = 1; i <= 30; i++){

    (i > 1)? total += (money *= 2): total;
    (total >= 10000 && (total - money)< 10000)? console.log("He makes $10,000 after " + i + " days. The actual amount on that day is: $" + total.toFixed(2)) : null ;
    (total >= 1000000000 && (total - money) < 1000000000)? console.log("He makes 1 billion after " + i + " days. The actual amount on that day is: " + total.toFixed(2)) : null ;
    money = total;
}
console.log("After " + (i-1) + (((i-1)> 1)? " days, he makes $" : " day, he makes $") + total.toFixed(2));

var j = i;

while (total < Number.MAX_VALUE){

    total += (money *= 2);
    money = total;

    j++;
}

console.log("He reach " + total + " money after " + (j-1) + " days");