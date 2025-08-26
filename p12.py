a = 5
b = 2
print(a / b)
print(a // b)
print('*' * 40)

a = [9, 6]
b = [2, 1, 3]
print(b + a)
print(b * 3)
print('*' * 40)

print(id(a))
a = a + b
print(id(a))
a += b
print(id(a))
a = a + b
print(id(a))
print('*' * 40)

print(id(b))
b = a
print(id(a))
print(id(b))
print('*' * 40)

tup1 = (1, 2)
tup2 = (3, 4, 5)
print(tup1 + tup2)
tup1 += tup2
print(tup1)
print('*' * 40)

d = {'name': 'zs', 'age': 12}
c = d
c['age'] = 50
print(c)
print(d)
print(id(c))
print(id(d))