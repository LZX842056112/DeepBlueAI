# string = 'hello world', 如何切片可以输出 'hello w'?
string = 'hello world'
string[:7]

# string = 'hello world', 如何切片(不是索引)可以输出空格字符?
string[5:6]

# string = 'hello world', 如何切片(不是索引)可以输出 'd'?
string[-1:]

# string = 'hello world', string[5:-1]的结果是什么?
'worl'

# string = 'hello world', string[1:9:2]的结果是什么?
'el o'

# string = 'hello world', string[-2:4:-2]的结果是什么?
'lo '

"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并做格式化输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
根据用户输入数据计算出总价为: 10.2684

请用三种字符串格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""

# 输入
fruit = input("请输入水果品种: ")
price = float(input("请输入水果单价(元/kg): "))
weight = float(input("请输入水果重量(kg): "))

# %格式化
print('您购买了%.2fkg的%s, 单价为%.2f元/kg, 您需要支付%.2f元!' % (weight,fruit, price, price * weight))
# format格式化
print('您购买了{:.2f}kg的{}, 单价为{:.2f}元/kg, 您需要支付{:.2f}元!'.format(weight,fruit, price, price * weight))
# f-string格式化
print(f'您购买了{weight:.2f}kg的{fruit}, 单价为{price:.2f}元/kg, 您需要支付{weight * price:.2f}元!')
