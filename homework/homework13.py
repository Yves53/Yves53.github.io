import random


def coin_toss():
    t = 5000
    head_count = 0
    tail_count = 0
    print "Starting the program..."
    for i in range(0, t):
        num = random.randint(0, 1)
        side = "head" if num == 0 else "tail"
        head_count += 1 if num == 0 else 0
        tail_count += 1 if num == 1 else 0
        print "Attempt #", (i + 1), ": Throwing a coin... It's a", side, "! ... Got",\
            head_count, "head(s) so far and", tail_count, "tail(s) so far"

coin_toss()
