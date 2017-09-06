a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = "It's thanksgiving day. It's my birthday,too!"
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
y = [x[0], x[-1]]
z = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
z.sort()
num = len(z)/2
new_arr = z[:num]
z = z[num:]
z.insert(0, new_arr)
print min(a)
print max(a)
print words.find('day')
print words.replace('day', 'month', 1)
print x[0] + ' ' + x[-1]
print y
print z
