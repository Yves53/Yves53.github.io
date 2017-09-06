def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    sqr = int(n ** 0.5)
    f = 5
    while f <= sqr:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        # loop every 6th integer
        f += 6
    return True


def is_square(p):
    sqr = int(p**0.5)
    if sqr**2 == p:
        return True


for num in range(100, 100000):
    if not is_square(num) and not is_prime(num):
        print 'FooBar'

    elif is_prime(num):
        print 'Foo'

    elif is_square(num):
        print 'Bar'

