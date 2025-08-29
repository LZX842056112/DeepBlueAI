"""
实现程序：请用户输入一个正整数 n, 程序计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例:
输入: n = 234
输出: 15 

解释:
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15
"""
multiply = 1
total = 0
num_str = input('请输入一个正整数: ')
if num_str.isdigit():
    for i in num_str:
        num = int(i)
        multiply *= num
        total += num
    print(f'各位数字之积:\t{multiply}\n各位数字之和:\t{total}\n两数之差:\t\t{multiply-total}\n')
else:
    print('输入错误,请输入一个正整数!')


"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = (112.1+4j)
"""
def num_check(n):
    return type(n) is int or type(n) is float or type(n) is complex or type(n) is bool

d = {'a': 100, (): '9', 8.1: 'b', True: 3 + 4j}
total = 0
for k, v in d.items():
    if num_check(k):
        total += k
    if num_check(v):
        total += v
print(f'键和值中所有数字类型的数据之和: {total}')
