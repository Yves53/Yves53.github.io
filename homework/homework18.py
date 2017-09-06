def make_dict(arr1, arr2):
    x = arr1
    y = arr2
    if len(arr1) < len(arr2):
        x = arr2
        y = arr1
        for e in range(len(x) - len(y)):
            y.append(None)

    new_dict = {}
    for i in range(len(x)):
        new_dict[x[i]] = y[i]
    return new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dolphins", "llamas"]

print make_dict(name, favorite_animal)
