array = [1, 2, 3, 4, 5, 6]

def savl(arr):
    for i in range(0, (len(arr)-1)):
        arr[i] = arr[i+1]
    arr[-1] = 0
    return arr

print savl(array)
