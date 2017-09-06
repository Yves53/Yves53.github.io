array = [1, 2, -3, -5, 6, 7, -10]


def ssfan(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    return arr

print ssfan(array)
