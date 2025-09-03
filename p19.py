def outer(a):
    b = 700

    def inner(c):
        return a + b + c + e

    return inner


e = 200
f = outer(500)
print(f(800))
print('*' * 40)


def outer(a):
    b = 700

    def inner(c):
        return a + b + c + e

    return inner


e = 200
f = outer(500)
print(f(800))
print('*' * 40)


def outer():
    global a, b
    a, b, c, d = 3, 4, 5, 6
    print(a, b)

    def inner():
        global a, b
        nonlocal c, d
        a, b, c, d = 7, 8, 9, 0

    inner()
    print(c, d)


a, b = 1, 2
outer()
print(a, b)
