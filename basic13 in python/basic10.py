def printAv(arr):
    num = 0
    for i in arr:
        num += i
    return 1.0 * num/len(arr)

print "%1.2f" % printAv([5, 3, 8, 6, 9, 25])
