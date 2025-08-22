lst = []
print(lst)
print(len(lst))
lst = [4864, 'adsasd', [True, 2556.56], 3 + 4j]
print(lst)
print(len(lst))
print(list({1: 2, 3: 4}))
print(list({'a', 'b', 'c', 789, 456}))
print('*' * 40)

lst[0] = 'qwe'
lst[1:3] = None, ''
print(lst)
lst[1:3] = (None, '')
print(lst)
lst[1:3] = [None, '']
print(lst)
lst[0:1] = ['abc']
print(lst)
lst[0:1] = (123,)
print(lst)
lst[0:1] = 'qw'
print(lst)
lst[1::2] = '12'
print(lst)
lst[0:2] = ''
print(lst)
lst[len(lst):] = '🐉🐍'
print(lst)
print('*' * 40)

lst = list('123')
print(lst)
print(type(lst))
s = str(lst)
print(s)
print(type(s))
s = ''.join(lst)
print(s)
print('*' * 40)

lst = list((12, '45', True))
print(lst)
print(s)
print('*' * 40)

lst.append(['qwe', False])
print(lst)
lst.extend([5, 'a'])
print(lst)
print(lst[len(lst):])
print('*' * 50)

lst.insert(1, 888)
lst.insert(-1, 888)
print(lst)
print('*' * 40)

print(lst[::-1])
lst.reverse()
print(lst)
print('*' * 40)

print(lst.count(888))
print(lst.count(['qwe', False]))
print(lst[3].count(False))
print('*' * 40)

print(lst.index(888))
print(lst.index(888,2))
print('*' * 40)

print(lst.pop())
print(lst.pop(1))
print(lst)
print('*' * 40)

lst.append('a')
lst.remove('a')
print(lst)
print('*' * 40)

lst2 = lst.copy()
print(lst[:])
print(lst2)
lst2.clear()
print(lst2)
print(lst)
