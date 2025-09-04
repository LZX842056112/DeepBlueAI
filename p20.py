# 把大象放入冰箱

class elephant:
    def __init__(self):
        print('大象', end='')

    def into(self):
        print('进入', end='')
        fridge()
        print()


class fridge:
    def __init__(self):
        print('冰箱', end='')

    def open(self):
        print('开门')

    def close(self):
        print('关门')


class Person:
    def __init__(self, name):
        self.n = name
        print(self.n, end='')

    def open(self):
        print('打开', end='')
        fridge().open()

    def set(self):
        print('操作', end='')
        elephant().into()

    def close(self):
        print('关闭', end='')
        fridge().close()


Person('zs').open()
Person('zs').set()
Person('zs').close()
print('*' * 40)

p = 'zs'
print(f'{p}打开冰箱开门')
print(f'{p}操作大象进入冰箱')
print(f'{p}关闭冰箱关门')
print('*' * 40)


def get_up(name):
    print(f'{name}睁开眼睛')
    print(f'{name}起身')
    print(f'{name}穿好衣服')


def wash(name):
    print(f'{name}刷牙')
    print(f'{name}洗脸')


def eat(name):
    print(f'{name}吃菜')
    print(f'{name}扒饭')


def login_id(name):
    print(f'{name}输入账号密码')
    print(f'{name}登陆账号成功')


def study(name):
    print(f'{name}看视频')
    print(f'{name}查资料')
    print(f'{name}写代码')


def sleep(name):
    print(f'{name}脱掉外套')
    print(f'{name}躺下')
    print(f'{name}闭上眼睛')


count_s = 0
stu1 = '张三'
age1 = 18
grade1 = '高三'
print(f'大家好! 我是{stu1}, 今年{age1}岁, 目前正在读{grade1}!')
count_s += 1
get_up(stu1)
wash(stu1)
eat(stu1)
login_id(stu1)
study(stu1)
eat(stu1)
study(stu1)
eat(stu1)
wash(stu1)
sleep(stu1)
print(f'当前统计的学生人数为: {count_s}')
print('*' * 40)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


stu1 = Student('张三', 18, 2)
stu2 = Student('李四', 20, 3)
stu3 = Student('王五', 15, 1)
print(stu1)
print(stu2)
print(stu3)
print(type(stu1))
print(type(stu2))
print(type(stu3))
print('*' * 40)
