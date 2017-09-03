 msg = 'codingdojo'
for (var x = 1; x < msg.length - 1; x++) {
    if (msg.length === 2) {
        for (var i = 3; i < 5; i++) {
            console.log(i);
        }
    }
    else {
        for (var i = msg.length; i > (msg.length - 1); i--) {
            console.log(i)
        }
    }
}
/*
for (var x = 20; x > 6; x--){
    console.log(x);
    break;
}

var msg = 'dojo';
if(msg === 'dojo')
{
    console.log('coding'+msg);
}
else
{
    console.log('ninja'+msg)
}

msg = 'hello!';
for(var x = 21; x > msg.length + 4; x--){
    console.log(x)
}
var g = 10;
if (g === 10){
    console.log(g);
}
else {
    console.log('Hello');
}*/