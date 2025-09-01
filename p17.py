def add1(left, right):
    pass


print(add1(1, 2))
print('*' * 40)


def add2(left, right):
    print(left + right)
    return


print(add2(1, 2))
print('*' * 40)


def add3(left, right):
    return left, right


print(add3(1, 2))
print('*' * 40)


def func(b):
    print(id(a), a)
    print(id(b), b)


a = 789
func(a)
print('*' * 40)


def func(b):
    print(id(a), a)
    print(id(b), b)


a = [789]
func(a)
print('*' * 40)


def func(b):
    b.append(345)


a = [789]
func(a)
print(a)
print('*' * 40)


def func(a, b, c=6):
    print(a - b - c)


func(3, 4)
func(3, 4, 5)
func(a=3, b=4, c=5)
func(b=4, c=5, a=3)
func(3, 4, c=5)
print('*' * 40)


def func(*args):
    print(args)


func()
func(3, 1, 4, 6)
print('*' * 40)


def func(**kwargs):
    print(kwargs)


func()
func(a=3, c=2, b=4)
print('*' * 40)


def func(*args, **kwargs):
    print(args)
    print(kwargs)


func()
func(1, 2)
func(a=3, b=4)
func(1, 2, a=3, b=4)
print('*' * 40)


def func(a, b, *d, c=100, e, **f):
    print(a, b, c, d, e, f)


func(1, 2, 3, 4, 5, e=6, g=7, h=8)
print('*' * 40)


def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


func(1, 2, 3, kwd1=4, kwd2=5)
func(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5)

'''
    / 限制在它之前的形参只能接收位置参数
    * 限制在它之后的形参只能接收关键字参数
'''
def f(a, b, /, c, *, d, e):
    print(a, b, c, d, e)


# f(a=1, b=2, c=3, d=4, e=5)
# f(1, b=2, c=3, d=4, e=5)
f(1, 2, c=3, d=4, e=5)
f(1, 2, 3, d=4, e=5)
# f(1, 2, 3, 4, e=5)
# f(1, 2, 3, 4, 5)
