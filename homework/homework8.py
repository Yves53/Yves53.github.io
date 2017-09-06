import sys
print "X 1 2 3 4 5 6 7 8 9 10 11 12"
for i in range(1, 13):
    print i,
    for j in range(1, 13):
        sys.stdout.write(" " + str(i * j))
    print '\n'




