import random


def grades():
    for i in range(0, 10):
        num = random.randint(60, 100)
        print 'The score is', num, 'Grade -',
        print ('D' if num <= 69 else 'C' if num <= 79 else 'B' if num <= 89 else 'A' if num > 89 else 'none')


grades()
