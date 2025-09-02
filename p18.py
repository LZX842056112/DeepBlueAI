import p17
import homework4.李宗效作业4

print((lambda: 'It just returns a string')())
f = lambda: 'It just returns a string'
print(f())

(lambda x, y, z: print(x + y + z))(1, 2, 3)
f = lambda x, y, z: print(x + y + z)
f(1, 2, 3)

tup = (8, 5, -9, 6, 2)
print(sorted(tup, key=lambda x: -x if x < 0 else x))
print('*' * 40)

a, b, c = [4, 3, 'a']
print(a)  # 4
print(b)  # 3
print(c)  # 'a'
print('*' * 40)

a, *b, c = 'hello'
print(a)  # 'h'
print(b)  # ['e', 'l', 'l']
print(c)  # 'o'
print('*' * 40)

a, *b, c = 'he'
print(a)  # 'h'
print(b)  # []
print(c)  # 'e'
print('*' * 40)

*a, = 'hel'
print(a)  # ['h', 'e', 'l']
_, *b, _ = [4, 3, 5, 7]
print(b)  # [3, 5]
print('*' * 40)


def func(a, b, c):
    print(a, b, c)


func(*{1, 2, 3})  # 等价于func(1, 2, 3)
d = {'a': 1, 'b': 2, 'c': 3}
func(*d)  # 等价于func('a', 'b', 'c')
func(**d)  # 等价于func(a=1, b=2, c=3)
print('*' * 40)


def f(*x):
    print(x)
    print(*x)


a = [5, 6, 7, 8]
f(a)
f(*a)
print('*' * 40)

print(p17.a is int)
print(homework4.李宗效作业4.a is int)
print('*' * 40)


def fun1(a):
    global num
    num = 666
    print(locals())
    print(globals())


def fun2(a):
    num = 777
    print(locals())
    print(globals())


def fun3(a):
    print(num)


num = 111
fun3(1)
print(num)
print('*' * 40)

fun1(1)
print(num)
print('*' * 40)

fun2(1)
print(num)
print('*' * 40)

print(globals())  # 返回全局命名空间
# 在全局作用域, locals()等价于globals()
print(locals())
print('*' * 40)

lst = [1, 2, 3]
print(sum(lst))
print(sum(tuple(lst)))
print(sum(set(lst)), 100)
print('*' * 40)

lst = ['1', '-2', '3.14']
m = map(float, lst)
print(list(m))
print('*' * 40)


def exam(a, b):
    return a ** b


iter1 = [3, 5, 2]
iter2 = [5, 2, 1]
iterator = map(exam, iter1, iter2)
print(list(iterator))
print('*' * 40)

iterator = map(lambda a, b: a ** b, iter1, iter2)
print(list(iterator))
print('*' * 40)

lst = [exam(i, j) for i, j in zip(iter1, iter2)]
print(lst)
print('*' * 40)

lst = [(lambda a, b: a ** b)(i, j) for i, j in zip(iter1, iter2)]
print(lst)
