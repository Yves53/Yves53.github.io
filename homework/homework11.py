def odd_even():
    for i in range(1, 21):
        if i % 2 == 0:
            print 'Number is', i, '. This is an even number'
        else:
            print 'Number is', i, '. This is an odd number'

odd_even()


def multiply(arr, num):
    arr = [i*num for i in arr]
    return arr

print multiply([2, 4, 10, 16], 5)


def layered_multiples(arr):
    arr2 = []
    e = 0
    for i in arr:
        for j in range(0, i):
            arr2.append(1)
        arr[e] = arr2
        e += 1
        arr2 = []
    return arr

print layered_multiples(multiply([2, 3, 4], 2))
