from random import random

a, b = 1, 32
print(a, b)

a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c = '123'
print(a, b, c)

a, b, c = {1: 1, 2: 2, 3: 3}
print(a, b, c)
print('*' * 40)

a = b = c = 999
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))
print('*' * 40)

a = b = c = [1, 2, 3]
print(id(a))
print(id(b))
print(id(c))
print('*' * 40)

b.append(4)
print(a)
print(b)
print(c)

a = 'k'
b = 8
c = ()
d = 0

print(c and a)
print(a and c)
print(d and c)
print(b and a)
print('*' * 40)

print(c or a)
print(a or c)
print(d or c)
print(b or a)
print('*' * 40)

print(not a)
print(not b)
print(not c)
print(not d)
print('*' * 40)

print(b and not a or c)
print('*' * 40)

a = 0
b = 1
c = ()
print(c and b / c)
print(b or a + c)
# print(b and a + c)
print('*' * 40)

tup = ('0', ' ', 'None', 'False', '[]')
print(all(tup))
tup = ('0', ' ', 'None', 'False', '')
print(all(tup))
print(all([]))
print('*' * 40)

tup = (0, '', None, False, [], 0j, set())
print(any(tup))
tup = (0, ' ', None, False, [], 0j, set())
print(any(tup))
print(any([]))
print('*' * 40)

tup = ()
print(all(tup))
print(any(tup))
print('*' * 40)

string = 'hello world'
print('l' in string)
print('' in string)
print(' ' in string)
print('a' in string)
print(',' in string)
print('*' * 40)

print('l' not in string)
print('' not in string)
print(' ' not in string)
print('a' not in string)
print(',' not in string)
print('*' * 40)

lst = [True, False, [2, 3], 4]
print(1 in lst)
print(False in lst)
print(2 in lst)
print([True, False] in lst)
print([2, 3] in lst)
print(None in lst)
print(None not in lst)
print('*' * 40)

d = {1: 2, 0: 4}
print(True in d)
print(False in d)
print(2 not in d)
print(4 not in d)
print('*' * 40)

a = 256
b = 256
print(a == b)
print(a is b)
print(id(a) == id(b))
print('*' * 40)

a = [257, 1]
b = [257, 1]
print(a == b)
print(a is b)
print(id(a) == id(b))
b = a
print(a == b)
print(a is b)
print(id(a) == id(b))
print('*' * 40)

a = (1, 2, 3, {})
b = (1, 2, 3, {})
print(id(a))
print(id(b))
print(a is b)
b = a
print(a is b)

a = (1, 2, 3)
b = (1, 2, 3)
print(id(a))
print(id(b))
print(a is b)
print('*' * 40)

# 下面v1,v2的值分别是多少？为什么？
v1 = 3
v2 = v1
print("v1在内存的地址：%d,v2在内存中地址:%d" % (id(v1), id(v2)))
v1 += 2
print("v1在内存的地址：%d,v2在内存中地址:%d" % (id(v1), id(v2)))
print("v1:", v1)
print("v2:", v2)
print('*' * 40)

# 下面l2的值又是多少？为什么？
l1 = [1, 2, 3]
l2 = l1
print("l1在内存的地址：%d,l2在内存中地址:%d" % (id(l1), id(l2)))
print(l2)
print("l1在内存的地址：%d,l2在内存中地址:%d" % (id(l1), id(l2)))
l1.append(4)
print(l2)
print("l1在内存的地址：%d" % (id(l1)))
print('*' * 40)

str1 = 'hahhahah'
str2 = str1
str1 += "123"
print(str1, str2)
print('*' * 40)

a, b = float(random()), float(random())
print(f'a: {a}, b: {b}')
if a == b:
    print('a == b')
elif a > b:
    print('a > b')
else:
    print('a < b')