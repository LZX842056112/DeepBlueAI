d = {'name': 'Tom', 'age': 'aa'}
print(d)
print(d['age'])
# print(d['a'])
d['age'] = 29
d['weight'] = 62
print(d)
del d['weight']
print(d)
print(dict(['ab', 'cd', 'ef']))
d = dict(name='Tom', age=28)
print(d)
d = dict([('name', 'Tom'), ('age', 28), [12.3, 14], (12.3, 18)])
print(d)
d = dict(zip(['name', 'age'], ['zs', 12]))
print(d)
print('*' * 40)
res = zip('abcd ', [1, 2, 3, 4, 5], (9, 8, 7))
print(res)
# print(res[1])
print(next(res))
res2 = tuple(res)
print(list(res2))
print(list(res))
print('*' * 40)


def exam(*a, **b):
    print(a)
    print(b)


exam()
exam(1)
exam(1, 45, 456, 465, 46)
print('*' * 40)

d['score'] = 100
keys = d.keys()
values = d.values()
items = d.items()
length = len(d)
print(keys)
print(values)
print(items)
print(length)

lst_keys = list(keys)
lst_values = list(values)
lst_items = list(items)
print(lst_keys)
print(lst_values)
print(lst_items)

del d['score']
print(d)
print(keys)
print(values)
print(items)
print(length)
print(len(d))
print(lst_keys)
print(lst_values)
print(lst_items)
print('*' * 40)

print(d['age'])
print(d.get('age'))
print(d.get('aa', False))
print(d.setdefault('age', 0))
print(d.setdefault('cc', 0))
print(d)
print('*' * 40)

d.update([('age', 25), ('name', 'ls'), ('weight', 62)])
print(d)
d.update(cc=45, name='tom', height=75)
print(d)
d.update()
print(d)
print('*' * 40)

print(d.pop('height', '00'))
print(d)
print(d.pop('aa', '123'))
print('*' * 40)

print(d.popitem())
print(d)
d.clear()
print(d)
print('*' * 40)
print('*' * 40)

s = {789, 12.5, False, 3 + 4j, 'hello', 12.5, (1456, 'asd')}
print(s)
print(len(s))
print(set())
print(set("hel lo"))
print(set([1, 2, 3]))
print(set((1, 2, 3)))
# 字典作为一个iterable, 只有键参与迭代
print(set({1: 2, 3: 4}))
print('-'.join(set("hel lo")))
print(tuple(s))

s.update('abc', [1, 2, 3], (2, 3, 4))
print(s)
print('*' * 40)

s.add('hello world')
print(s)
s.remove('c')
print(s)
print('*' * 40)

s.discard('a')
s.discard('k')
print(s)
print('*' * 40)

copy = s.copy()
print(copy)
print(s)
print('*' * 40)

s.pop()
print(s)
print('*' * 40)

s.clear()
print(s)