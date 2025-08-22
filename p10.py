lst = [4864, 3, 132]
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))

print('*' * 40)

lst = [3.14, 1.2, 5.6]
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))
print('*' * 40)

lst = ['b', 'f', 'a', '1', ' ', '好']
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))

print(chr(65))
print(ord('A'))
print('*' * 40)

lst = [['a', 'z'], ['f'], ['a', 'x'], ['1'], [' '], ['好']]
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))
print('*' * 40)

lst = [('b',), ('f',), ('a', 5), ('1',), (' ',), ('a', 1)]
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))
print('*' * 40)

lst = [True, False, True]
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print(sorted(lst, reverse=True))
print('*' * 40)

print(abs(-9))
print(abs(True))  # 1
print(abs(False))  # 0
print(abs(3 + 4j))  # 求模, 5.0

lst = [5, -9, 1, -6]
lst.sort(key=abs)
print(lst)
print(sorted(lst, key=abs))
lst.sort(key=abs, reverse=True)
print(lst)
print(sorted(lst, key=abs, reverse=True))


def fun(num):
    if num < 0:
        return -num
    return num


lst = [5, -9, 1, -6]
lst.sort(key=fun)
print(lst)
print(sorted(lst, key=fun))
lst.sort(key=fun, reverse=True)
print(lst)
print(sorted(lst, key=fun, reverse=True))
print('*' * 40)

lst = ['4864', '3', '132']
lst.sort(key=int)
print(lst)
print(sorted(lst, key=int))
lst.sort(key=int, reverse=True)
print(lst)
print(sorted(lst, key=int, reverse=True))
print('*' * 40)

lst = ('4864', '3', '132')
# lst.sort(key=int)
print(lst)
print(sorted(lst, key=int))
# lst.sort(key=int, reverse=True)
# print(lst)
print(sorted(lst, key=int, reverse=True))
print('*' * 40)

lst = {'4864': 12, '3': 34, '132': 56}
# lst.sort(key=int)
print(lst)
print(sorted(lst, key=int))
# lst.sort(key=int, reverse=True)
# print(lst)
print(sorted(lst, key=int, reverse=True))
print('*' * 40)

s = 'acdfg'
print(sorted(s))
print(s)
print('*' * 40)

lst = ['4864', '3', '132']
x = lst
print(id(lst))
del lst[0], lst[1:2]
print(id(lst))
print(id(x))
print(lst)
print(x)
print('*' * 40)

lst = ['4864', '3', '132', '94849', 5 + 54j]
del lst[1::3]
print(lst)
x = lst
print('*' * 40)

lst.clear()
print(lst)
print(x)
print(id(lst))
print(id(x))
print('*' * 40)

tup = 1,
print(tup)
tup = ()
print(tup)
tup = 132, 'asa', True, ['qw', False, 564], 3 + 4j, 132
print(tup)
tup = (132, 'asa', True, ['qw', False, 564], 3 + 4j, 132)
print(tup)
print(len(tup))
tup[3][0] = '52'
print(tup)
print('*' * 40)

print(type(tup))
print(tuple)
print(list())
print(tuple())
print(tuple('465asdas'))
lst = list(tup)
print(lst)
tup = tuple(lst)
print(tup)
print(tup.count(132))
print(tup.index(132, 1))
print('*' * 40)

d = {'name': 'Tom', 'age': 28, True: [12]}
print(d)
print(len(d))
d = {}
print(d)
d['name'] = 'Tom'
d['age'] = 29
d[12.5] = 13
print(d)
d = {}
print(d)
d = dict(name='Tom', age=30)
print(d)
d = {}
print(d)
d = dict([('name', 'Tom'), ('age', 28), (12.3, 14), (12.3, 18)])
print(d)
print('*' * 40)

print(d.keys())
print(d.values())
print(d[12.3])
print(d.get(12.3))
print('*' * 40)

d = {'name': 'Tom', 'age': 28}
print('🐉'.join(d))

st = [1, 2]
print(st)
st.extend(d)
print(st)
print(d)
