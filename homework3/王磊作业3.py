""" 
请用户输入身高(m)和体重(kg), 并根据BMI公式(体重/身高的平方)计算出的BMI指数来判断用户的体重情况
判断标准：
BMI >= 35 为重度肥胖
30 <= BMI < 35 为中度肥胖
27 <= BMI < 30 为轻度肥胖
23 <= BMI < 27 为超重
18.5 <= BMI < 23 为正常体重
BMI < 18.5 为轻体重
"""
height = float(input("请输入身高(m):"))
weight = float(input("请输入体重(kg):"))
BMI = weight / (height ** 2)
print(BMI)
if BMI > 35:
    print('重度肥胖')
elif 30 <= BMI < 35:
    print('中度肥胖')
elif 27 <= BMI < 30:
    print('轻度肥胖')
elif 23 <= BMI < 27:
    print('超重')
elif 18.5 <= BMI < 23:
    print('正常体重')
else:
    print('轻体重')




""" 
请用户输入三个不同的整数, 输入时用空格隔开, 利用条件语句判断出这三个整数中的最大值
"""
a, b, c = input("请输入三个不同的整数，使用空格进行分隔:").split(' ')
max_ = int(a)
if int(b) > max_:
    max_ = int(b)
if int(c) > max_:
    max_ = int(c)
print(max_)

