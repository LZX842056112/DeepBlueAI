score = float(input('你这次考试考了多少分? '))
res = '厉害!' if score >= 90 else \
    '优秀!' if score >= 80 else \
        '良好!' if score >= 70 else \
            '及格!' if score >= 60 else \
                '不及格!'
print(res)

print('*' * 40)
d = {'石头': 0, '剪刀': 1, '布': 2}
computer = set(d).pop()
player = input('请出拳: ')
if player not in ('石头', '剪刀', '布'):
    print('请输入正确')
else:
    print(f'电脑：{computer}, 玩家：{player}')
    if d[computer] == d[player]:
        print('平局')
    elif d[computer] - d[player] in (-1, 2):
        print('电脑胜')
    else:
        print('玩家胜')

print('*' * 40)
num = 1
while num <= 5:
    print(num)
    num += 1

print('*' * 40)
num = 1
while num <= 10:
    if not num % 2:
        print(num)
    num += 1

print('*' * 40)
num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print(total)

print('*' * 40)
num = 1
total = 1
while num <= 10:
    total *= num
    num += 1
print(total)

print('*' * 40)
num = 1
while num <= 100:
    # if '4' not in str(num):
    # if num % 10 != 4 and num // 10 != 4:
    if 4 not in (num % 10, num // 10):
        print(num)
    num += 1
