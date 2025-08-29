num = 100
while num <= 108:
    print(num)
    num += 1
print('*' * 40)

num = 100
while True:
    print(num)
    num += 1
    if num > 108:
        break
print('*' * 40)

num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print(f'{num2} x {num1} = {num1 * num2}\t', end='')
        num2 += 1
    num1 += 1
    print()
print('*' * 40)

str1 = 'qwe'
str1 = str1.center(5, '*')
print(str1)
str1 = str1.ljust(10, '+')
print(str1)
str1 = str1.rjust(15, '0')
print(str1)

print('*' * 40)
lst = [321, 'qwe', True, {1, 'as'}, {'a': 1, 'b': 2}, (123, 'abc')]
for i in lst:
    print(i)

for i in lst[1]:
    print(i)
for i in lst[4]:
    print(i)
for i in lst[3]:
    print(i)
for i in lst[len(lst) - 1]:
    print(i)

print('*' * 40)
res = zip('abcd', [4, 5, 7, 1])
for i in res:
    print(i)

for i in range(-4, 10, 2):
    print(i)


r = range(-4, 10, 2)
print(r)
print(len(r))
print(r[-1])
print(list(r))
print(tuple(r))
print(r[::3])
print(r[:4])
print(r[2:])
print(r[2:-4:-1])
print('*' * 40)

r = range(-6)
print(r)
print(len(r))
