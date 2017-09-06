def typeList(arr):
    s = 0
    bln_s = False
    bln_string = False
    string = ''

    for i in range(0, len(arr)):
        if type(arr[i]) == int:
            bln_s = True
            s += arr[i]
        else:
            bln_string = True
            string += arr[i]
    if bln_string and bln_s:
        print 'The array is mixed; the sum is:', s, ' and the concatenated string is ', string
    elif bln_s:
        print 'There are no strings, it contains only numbers that add up to:', s
    elif bln_string:
        print 'There are no numbers, it contains only strings that concatenate to:', string
    else:
        print 'The array is empty'

typeList([1,3,6,'a','b'])
