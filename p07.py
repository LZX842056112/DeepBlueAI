s = '12345'
print(s[3])
print(s[-5])
print(s[-len(s) + 1])
print(len(s))
print(s[1:4:2])
print(s[4:1:-2])
print(s[-4:-1])
print(s[:4:2])

print('*' * 30)

lst = [1, 'xx', [33.4, True], 4 + 3j, 521]
print(lst)
print(len(lst))
print(lst[2][1])
print(lst[-len(lst)])
print(lst[1:4:2])
print(lst[4:1:-2])
print(lst[-4:-1])
print(lst[:4:2])

print('*' * 30)

tup = (1, 'xx', [33.4, True], 4 + 3j, 521)
print(tup)
print(len(tup))
print(tup[2][1])
print(tup[-len(tup)])
print(tup[1:4:2])
print(tup[4:1:-2])
print(tup[-4:-1])
print(tup[:4:2])

print('*' * 30)

print('aaaaa%s,%d' % ('1', 2))
num = 1
num2 = 2
print(f'aaaaa{num},{num2}')

print('*' * 30)

print(f'{123}5555555555''{}''')

name = input('name: ')
age = int(input('age: '))
height = float(input('height: '))
weight = float(input('weight: '))
print(f'name: {name}, age: {age}, height: {height:.2f}m, weight: {weight:.2f}kg')
print('name: %s, age: %d, height: %.2fm, weight: %.2fkg' % (name, age, height, weight))
print('name: {}, age: {}, height: {:.2f}m, weight: {:.2f}kg'.format(name, age, height, weight))
print('name: {1}, age: {0}, height: {2:.2f}m, weight: {3:.2f}kg'.format(age, name, height, weight))
print('name: {name}, age: {age}, height: {height:.2f}m, weight: {weight:.2f}kg'.format(age=age, name=name, height=height, weight=weight))

