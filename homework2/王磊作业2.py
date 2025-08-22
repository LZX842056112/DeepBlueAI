# 给定时间字符串 t = "2025/10/28-14:35:48"，提取月份和分钟数并计算它们的乘积
t = "2025/10/28-14:35:48"
month = t.split('/')[1]             # 10
minute = t.split(':')[-2]           # 35
res1 = int(month) * int(minute)     # 350

# 给定字符串 s = "12a3a4AA5A"，求出'A'字符和'a'字符的数量差
s = "12a3a4AA5A"
count_A = s.count('A')      # 3
count_a = s.count('a')      # 2
res2 = count_A - count_a    # 1

# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引
lst = [1, 3, 2, 6, 1, 1, 41]


def last_item_index(lst, item):
    return len(lst) - lst[::-1].index(item) - 1


res3 = last_item_index(lst, 1)  # 5
# print(res3)

"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据

例:
用户输入:  1,2,3,45,678
程序输出:  ('1', '2', '3', '45', '678')
"""


def input2tuple(sep=','):
    user_input = input(f"请输入数字(使用{sep}进行分隔,回车结束输入):\n")
    print(tuple(user_input.split(sep)))


# input2tuple()

"""
实现程序:
用户输入一串小写的英文字母, 求出英文字母有几种？并格式化输出

例如： 
输入 agbcppdcdho    输出：其中有 a b c d g h o p 8种英文字母
"""


def count_alpha():
    input_str = input("请输入字符串:\n")
    # 去重
    str2set = set(input_str)
    # 统计去重后元素个数
    count_res = len(str2set)
    # 排序并转换为字符串
    set2lst = sorted(list(str2set))
    str_res = ' '.join(set2lst)
    print(f'其中有 {str_res} {count_res}种英文字母')


count_alpha()
