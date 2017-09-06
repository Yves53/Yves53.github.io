def findChar(arr, string):
    print [i for i in arr if i.find(string) > 0]

findChar(['hello','world','my','name','is','Anna'], 'o')
