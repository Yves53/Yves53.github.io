function numbersOnly(arr) {

    newArray = [];
    var j = 0;
    for (var i = 0; i < arr.length; i++) {

        if (typeof arr[i] === 'number') {
            newArray[j] = arr[i];
            j++;
        }
    }

    console.log(newArray)
}

numbersOnly([1, "apple", -3, "orange", 0.5]);