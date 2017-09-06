import turtle
yves = turtle.Pen()
yves.shape('turtle')
DIST = 100
for x in range(0, 1000):
    print "x", x
    for y in range(1, 5):
        print "y", y
        yves.left(45)
        yves.forward(DIST)
        yves.color('blue')
        yves.circle(100)
        yves.color('yellow')
        yves.circle(-100)


    DIST += 1
