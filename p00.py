'''
问题4描述：
给定一个嵌套列表 nested_lst（列表中的元素可能是列表或普通值），编写
一个函数 get_nested_element，接收 nested_lst 和一个索引列表
indices（如 [i, j, k] 表示访问 nested_lst[i][j][k]），返回对
应位置的元素。若索引路径无效（如中间某层不是列表，或索引超出范围），返回 None。

示例：

输入：nested_lst = [1, [2, 3], [4, [5, 6]]], indices = [2, 1, 0] → 输出：5
输入：nested_lst = [1, [2, 3], [4, [5, 6]]], indices = [0, 1] → 输出：None（因 nested_lst[0] 是整数，不是列表）
'''

# def get_nested_element(nested_lst, indices):
#     for i in range(len(indices)):
#         if type(nested_lst) is int and len(indices) - 1 == i:
#             return None
#         index = indices[i]
#         if index > len(nested_lst):
#             return None
#         nested_lst = nested_lst[index]
#     return nested_lst
#
#
# lst = [1, [2, 3], [4, [5, 6]]]
# indie = [2, 1, 0, 1]
# print(get_nested_element(lst, indie))

# p14 用到这个
a = int

'''
斐波那契系数
[0,1,1,2,3,5,8...]
'''

lst = [0, 1]


def func(num):
    if num == 1:
        return str([0])
    if num == 2:
        return str(lst)
    for i in range(num - 2):
        lst.append(lst[-1] + lst[-2])
    return str(lst)


print(func(10))


def get_rabbits(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


for i in range(1, 11):
    print(get_rabbits(i), end=' \t')

print()


def get_rabbits():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


g = get_rabbits()
for _ in range(10):
    print(next(g), end=' \t')
