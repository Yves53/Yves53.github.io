# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for j in range(1, 1001, 2):
    print j

# Create another program that prints all the multiples of 5 from 5 to 1,000,000.
print [i for i in range(5, 1000001, 5)]

# Create a program that prints the sum of all the values in the list:
l = [1, 2, 5, 10, 255, 3]
n = 0
for k in l:
    n += k
print n

# Create a program that prints the average of the values in the list:
li = [1, 2, 5, 10, 255, 3]
m = 0
for p in li:
    m += p
print "%1.2f" % (1.0*m/len(li))
