array = [1, 2, 3, 4, 5, 6]


def mma(arr):
    mini = arr[0]
    maxi = arr[0]
    s = 0
    for i in arr:
        if mini > i:
            mini = i
        if maxi < i:
            maxi = i
        s += int(i)
    print "The min is ", mini, " the max is ", maxi, " the average is %1.2f" % (1.0 * s/len(arr))

mma(array)

