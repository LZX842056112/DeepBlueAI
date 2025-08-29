import pprint

lst = [321, 'qwe', True, {1, 'as'}, {'a': 1, 'b': 2}, (123, 'abc')]
for i in range(len(lst) - 1):
    item = lst[i]
    print(i, item, sep=',')

print('*' * 40)
print(enumerate)
str1 = 'lstaa'
e = enumerate(str1)
print(e)
for i, item in e:
    print(i, item)

print('*' * 40)
e = enumerate(str1)
for i in range(len(str1)):
    print(next(e))
e = enumerate(str1)
print(list(e))
print('*' * 40)
e = enumerate(str1)
print(tuple(e))

e1 = enumerate({'a': 5, 'b': 6, 'c': 7})
print(list(e1))

print('*' * 40)
tup = ('abc', [1, 2, 3], {'a': 5, 'b': 6, 'c': 7}, ('x', 'y', 'z'))
for a, b, c in tup:
    print(a, b, c)

print('*' * 40)
for _ in range(3):
    print('hello')

print('*' * 40)
num = 0
while num < 50:
    num += 1
    if '4' in str(num):
        continue
    print(num)

print('*' * 40)
for i in range(1, 51):
    if '4' in str(i):
        continue
    print(i)

print('*' * 40)
for i in range(1, 51):
    if '4' in str(i):
        pass
    else:
        print(i)

print('*' * 40)
for i in range(1, 51):
    if '4' in str(i):
        ...
    else:
        print(i)

print('*' * 40)
lst = [i ** 2 for i in range(1, 9, 2)]
print(lst)

print('*' * 40)
[print(f'{j}x{i}={i * j}') for i in range(5) for j in range(1, i + 1)]

print('*' * 40)
lst = [(i, i ** 2) for i in range(1, 9, 2)]
print(lst)

print('*' * 40)
s = {(i, i ** 2) for i in range(1, 9, 2)}
print(s)

s = {i + j for i in range(3, 4) for j in range(1, 6) if j % 2}
print(s)

print('*' * 40)
d = {i: i ** 2 for i in range(1, 9, 2)}
print(d)

d = {k: v for v in range(99) if v % 2 for k in range(4)}
print(d)
pprint.pprint(d)

# 生成器表达式
print('*' * 40)
g = (i ** 2 for i in range(1, 9, 2))
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(list(g))
print(tuple(g))

print('*' * 40)


def get_rabbits(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


for i in range(1, 11):
    print(get_rabbits(i), end=' \t')
print()
print('*' * 40)


# 只要函数中存在关键字yield，那么该函数就会变成生成器函数
# 生成器函数被调用时，不会执行函数体，而是返回一个生成器对象
# 当next(该生成器对象)会开始执行函数体，函数体执行到yield语句时，
# 会将yield后面跟着的对象返回给调用方，函数在该处挂起
# 当我下一次next(该生成器对象)，又会从上一次挂起处继续往后执行
def get_rabbits():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


g = get_rabbits()
for _ in range(10):
    print(next(g), end=' \t')
