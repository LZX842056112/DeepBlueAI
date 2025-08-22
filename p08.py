s = ' \t\n \tab\n    c \n \t \n'
print(s.strip())
print('*' * 40)

s = 'hello world'
print(s.replace('l', '9'))
print(s.replace('l', '9', 2))
print(s.replace('', '🐉'))
print('*' * 40)

print(s.strip('h'))
print(s.strip('d'))
print(s.strip('hel'))
print(s.strip('rld'))
print(s.strip('we hld'))
print(s.strip('whlde '))
print(s.strip('lde  wh'))
print('*' * 40)

print(s.startswith('hello world'))
print(s.startswith('hel'))
print(s.startswith(''))
print(s.startswith('el'))
print(s.startswith(('he', 'wo')))
print(s.startswith(('eh', 'wo')))
print(s.startswith('el', 1))
print(s.startswith('el', 1, 5))
print(s.startswith('el', 2, 5))
print('*' * 40)

print(s.endswith('hello world'))
print(s.endswith('ld'))
print(s.endswith(''))
print(s.endswith('l'))
print(s.endswith(('eh', 'rld')))
print(s.endswith(('he', 'wo')))
print(s.endswith('ld', 1))
print(s.endswith('lo', 1, 5))
print(s.endswith('el', 2, 5))
print('*' * 40)

s = '123'
print(s.isdigit())
s = '1.23'
print(s.isdigit())
s = '-123'
print(s.isdigit())
s = '12a23'
print(s.isdigit())
print('*' * 40)

s = ' abc  \nd   \tef'
print(s.split(' '))
print(s.split())
print()

s = 'hello world'
print(s.split(' '))
print(s.split(sep='l', maxsplit=2))
print(s.split('l', 2))
print(s.split('l'))
print(s.split('a'))
print('*' * 40)

print(s.join('--'))
print(s.join('---'))
print(s.join('****'))
print(s.join(['1', '2', '3', '4']))
print(s.join(('1', '2', '3', '4')))
print(s.join({'height': 175, 'weight': 65}))
print(s.join({'5', 'hello', '789', 'world'}))
print('*' * 40)

print(s.count('a'))
print(s.count('el'))
print(s.count('l', 2, 3))
print(s.count('l', 3))
s = 'aaaaa'
print(s.count('aa'))
print('*' * 40)

s = 'hello world'
print(s.find('a'))
print(s.find('lo'))
print(s.find('l', 2, 3))
print(s.find('l', 3))
print('*' * 40)
print(s.rfind('a'))
print(s.rfind('lo'))
print(s.rfind('l', 2, 3))
print(s.rfind('l', 3))
print('*' * 40)

# print(s.index('a'))
print(s.index('lo'))
print(s.index('l', 2, 3))
print(s.index('l', 3))
print('*' * 40)

# print(s.rindex('a'))
print(s.rindex('lo'))
print(s.rindex('l', 2, 3))
print(s.rindex('l', 3))
print('*' * 40)

s = 'hellO woRlD'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())