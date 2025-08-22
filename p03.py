print("执行第1行啦")
print(2 / 1)
print("执行第3行啦")
a = 123
print(a)


def func(left, right):
    print("执行第9行啦")
    print("执行第10行啦", left + right)
    print("执行第11行啦", left - right)
    print("执行第12行啦", left * right, left / right)
    print("执行第15行啦")


func(3, 4)
a = 124
print(a)
print("执行第19行啦")

def f(x, y, z):
    return x + y + z
#
#
# f1 = f(1, 2, 3)
# print(f1)
#
# f2 = f(1, z=2, y=3)
# print(f2)

# def sqrt(a, b):
#     return a ** (1 / b)
#
#
# print(sqrt(16, 2))
