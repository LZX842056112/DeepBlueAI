class Cat:
    pass

    # def __str__(self):
    #     return "🐱"

    def __str__(self):
        return '789'

    def __repr__(self):
        return "猫"


c = Cat()
print(c)
print([c])
print({c: str(c)})
print('*' * 40)
print('*' * 40)


def f(a, b):
    print(a + b)
    try:
        print(a - b)
        print(a / b)
        print(a * b)
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    except Exception as e:
        print(e)
    except:
        print('有错误')
    else:
        print('无错误')
    finally:
        print('finally')
    print(a + b)


f(5, 2)
print('*' * 40)
f(5, 0)
print('*' * 40)
f('a', 'b')
print('ending...')
print('*' * 40)

z = ZeroDivisionError()
print(z)
z = ZeroDivisionError([1, 2, 3])
print(z)
z = ZeroDivisionError('division by zero')
print(z)
print('*' * 40)


class MyZeroDivisionError(BaseException):
    # class MyZeroDivisionError:
    #     def __init__(self, describe=''):
    #         self.describe = describe

    # def __str__(self):
    #     return f'{self.describe}'
    pass


z = MyZeroDivisionError()
print(z)
z = MyZeroDivisionError([1, 2, 3])
print(z)
z = MyZeroDivisionError('division by zero')
print(z)
print('*' * 40)


def f(a, b):
    try:
        print(a - b)
        print(a * b)
        return
    finally:
        print('finally')
    print(a + b)


f(5, 0)
print('*' * 40)


def f(a, b):
    try:
        print(a - b)
        print(a * b)
    finally:
        return
        print('finally')
    print(a + b)


f(5, 0)
print('*' * 40)


def div(a, b):
    if b == 0:
        raise ZeroDivisionError('ERROE')
    print(a / b)


div(5, 0)
print('*' * 40)


def div(a, b):
    assert b != 0, 'error'
    if not b != 0:
        raise AssertionError('error')
    print(a / b)


div(4, 2)
div(4, 0)  # AssertionError
print('*' * 40)

import math as m
from math import floor as fl, gcd as g, ceil
from math import *

print(fl(-7.5))
print(m.floor(-7.5))
print(sin(pi / 6))
