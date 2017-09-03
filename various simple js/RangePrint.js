function printRange() {
    var numbers = " ";

    if (arguments.length === 1) {
        for (var i = 0; i < arguments[0]; i++) {
            numbers += (i.toString() + " ");
        }
    }

    else if (arguments.length === 2) {
        for (i = arguments[0]; i < arguments[1]; i++) {
            numbers += (i.toString() + " ");
        }
    }

    else if (arguments.length === 3) {
        for (i = arguments[0]; i < arguments[1]; i += arguments[2]) {
            numbers += (i.toString() + " ");
        }
    }
    console.log(numbers);
}

printRange(-10,-2);