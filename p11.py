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

