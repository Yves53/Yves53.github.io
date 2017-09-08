def agty(arr, y):
    count = 0
    for i in arr:
        if i > y:
            print i
            count += 1
    print "There are ", count, "number(s) greater than ", y


agty([1, 2, 3, 4], 2)
