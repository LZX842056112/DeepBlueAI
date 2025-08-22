import math

print(type('123'))
print(str)
print(type(3 + 3j))
print(float)

print('***********************************')
print(int())
print(int(1.9))
print(int(True))
print(int('234'))
print(type(int('234')))

print('***********************************')
print(round(3.1415926, 3))
print(round(3.5))

print('***********************************')
print(math.pi)
print(math.e)
print(math.ceil(7.1))
print(math.floor(7.9))

print('***********************************')
print(math.sin(math.pi / 6))
print(math.cos(math.pi / 3))
print(math.tan(math.pi / 4))

print('***********************************')
print(math.asin(0.5))
print(math.acos(0.5))
print(math.atan(0.5))

print('***********************************')
print(math.gcd(12, 9))
print(math.log(math.e ** 3))

print('***********************************')
print(math.sqrt(16))
print(math.isqrt(16))

print('***********************************')
print(float())
print(float(123))
print(float(12.3))
print(float(False))
print(float('12'))
print(type(float('1.2')))
print(int(float('2.5')))

print('***********************************')
print(bool())
print(bool(''))
print(bool(set()))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))
print(bool(0))
print(bool(3j))
print(bool('12'))

print(complex())
print(complex(3))
print(complex(3.2, 4))
print(complex(3, 4j))
print(complex('3.2+5j'))

print('*' * 30)
print(str(1).__eq__('1'))
print(str(7.8) == '7.8')
print([str()])
print([str(True)])
print([str(3 + 4j)])

print('***' * 10)

print([1233, '645', """52""", True == 1, 3 + 4j, 45.52])

s = 'a\\b'
print(s)
print([s])

print('***' * 10)
print()
print('qqqqqqqqqq', sep='--', end='.\n')
print(111.11111, 'qqqqqqqq', sep='-', end='.\n')
print(sep='-', end='.\n')

print('***' * 10)
res = input('hello\n')
print(res, '11', sep='-', end='.\n')
