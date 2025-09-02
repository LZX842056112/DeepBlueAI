"""
定义函数实现：
给定列表 numbers = [1, 3, 6, 5, 2, 9, 7, 8]，
函数返回一个新列表，其中每个偶数平方，奇数保持原值。
"""


def list_update(lst):
    return [i if i % 2 else i ** 2 for i in lst]


numbers = [1, 3, 6, 5, 2, 9, 7, 8]
print(list_update(numbers))

"""
定义函数实现: 
对于一个任意的整数, 判断其是否为回文整数(负整数不是回文整数)。
回文整数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如, 121 是回文, 而 123 不是。
"""


def palindrome_check(num_str):
    return num_str == num_str[::-1] if num_str.isdigit() else False


num_input = input('请输入一个任意的整数: ')
if palindrome_check(num_input):
    print(f'{num_input} 是回文整数')
else:
    print(f'{num_input} 不是回文整数')

"""
定义函数实现: 对于一个任意的正整数, 判断其是否为阿姆斯特朗数。

如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1**3 + 5**3 + 3**3 = 153。

1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


def armstrong_check(num_str):
    if num_str.isdigit() and int(num_str):
        total = sum(map(lambda x: int(x) ** len(num_str), num_str))
        if int(num_str) == total:
            return True
    return False


num_input = input('请输入一个任意的正整数: ')
if armstrong_check(num_input):
    print(f'{num_input} 是阿姆斯特朗数')
else:
    print(f'{num_input} 不是阿姆斯特朗数')

