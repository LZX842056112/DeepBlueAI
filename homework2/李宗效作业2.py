# 给定时间字符串 t = "2025/10/28-14:35:48"，提取月份和分钟数并计算它们的乘积
t = "2025/10/28-14:35:48"
month = int(t.split('/')[1])
minute = int(t.split(':')[1])
print(f'month: {month}')
print(f'minute: {minute}')
print(f'month * minute: {month * minute}')


# 给定字符串 s = "12a3a4AA5A"，求出'A'字符和'a'字符的数量差
s = "12a3a4AA5A"
print(abs(s.count('A') - s.count('a')))


# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引
lst = [1, 3, 2, 6, 1, 1, 41]
n = len(lst) - 1 - lst[::-1].index(1)
print(n)
print(lst[n])


"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据

例:
用户输入:  1,2,3,45,678
程序输出:  ('1', '2', '3', '45', '678')
"""
num_str = input('用户输入: ')
num_str = num_str.split(',')
print(f'程序输出:  {tuple(num_str)}')


"""
实现程序:
用户输入一串小写的英文字母, 求出英文字母有几种？并格式化输出

例如： 
输入 agbcppdcdho    输出：其中有 a b c d g h o p 8种英文字母
"""
# letter = input('输入：')
# letter_list = list(set(letter))
# letter_list.sort()
# letter_str = str(letter_list)
# letter_str = letter_str.strip('[').strip(']')
# letter_str = letter_str.replace(',', '').replace('\'', '')

letter = input('输入：')
letter_set = sorted(set(letter))
print(f'输出：其中有 {" ".join(letter_set)} {len(letter_set)}种英文字母')
