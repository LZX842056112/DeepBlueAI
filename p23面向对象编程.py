# 所有类都默认继承object, 通常不需要显式的表示
# 类, 类对象, 类型
class Student:

    # 类属性(类变量)
    school = 'xxx培训机构'

    # 方法: 在类中定义的函数
    # 魔术方法(特殊方法): 官方设计好的, 以两个下划线开头并且以两个下划线结尾来命名的方法
    # 魔术方法的特点: 魔术方法通常不需要主动的调用, 在特定情况下, 会被自动调用
    def __init__(self, name, age, grade):  # self: 实例对象2    name: '李四'   age: 19   grade: '大二'
        # 实例属性(实例变量)
        self.name = name    # 实例对象1.name = '张三'    # 实例对象2.name = '李四'   # 实例对象3.name = '王五'
        self.age = age      # 实例对象1.age = 18        # 实例对象2.age = 19        # 实例对象3.age = 20
        self.grade = grade  # 实例对象1.grade = '大一'   # 实例对象2.grade = '大二'  # 实例对象3.grade = '大三'

    # @staticmethod  # 内置的静态方法装饰器
    # def study(course):  # 静态方法
    #     return f'{Student.school}的学生在听{course}课!'

    # @property  # 内置的属性装饰器, 将方法装饰成一个只读属性, 属性名即方法名, 属性的值即方法的返回值
    # def get_all_attr(self):
    #     return self.name, self.age, self.grade

    # def study(self, course):  # 对象方法: 第一个参数位隐式的接收了调用该方法的实例对象
    #     return f'{self.name}在听{course}课!'

    # @classmethod
    # def study(cls, obj, course):
    #     return f'{obj.name}在听{course}课!'

    # @staticmethod
    # def study(obj, course):
    #     return f'{obj.name}在听{course}课!'

    @classmethod  # 内置的类方法装饰器
    def study(cls, course):  # 类方法: 第一个参数位隐式的接收了调用该方法的类对象
        print(f'{cls.school}的学生在听{course}课!')
        print(f'{Student.school}的学生在听{course}课!')


class Exam(Student):

    school = 'yyy培训机构'


Student.study('Python')
Exam.study('Python')


"""
__new__: 该魔术方法在实例化时被自动触发, 用来创建并返回实例对象的, 所以该方法又称之为 "构造方法"
__init__: 该魔术方法在实例化时被自动触发, 用来对实例对象做属性定制的, 所以该方法又称之为 "初始化方法"

每次实例化时, 都会先自动调用__new__(cls, *args, **kwargs)方法, 把要实例化的类对象(即: Student)
作为实参传递给形参cls, 实例化传入的其它实参(即: '张三', 18, '大一')传递给形参*args, **kwargs,
然后__new__方法就会根据形参cls接收到的类对象创建出一个对应的实例对象, 并返回该实例对象.

接着, 实例化还会自动调用__init__(self, name, age, grade), 把__new__方法创建的实例对象作为实参
传递给形参self, __new__接收到的其它参数(即: '张三', 18, '大一')分别传递给形参name, age, grade,
然后__init__方法就可以对形参self接收到实例对象做属性定制(inplace操作, __init__方法不能有返回值)
"""
# stu1 = Student('张三', 18, '大一')
# stu2 = Student('李四', 19, '大二')
# stu3 = Student('王五', 20, grade='大三')

# print(Student.study(stu1, 'Python'))
# print(Student.study(stu2, 'Python'))
# print(Student.study(stu3, 'Python'))
# print(stu1.study(stu1, 'Python'))
# print(stu2.study(stu1, 'Python'))
# print(stu3.study(stu1, 'Python'))

# print(stu1.study('Python'))
# print(stu2.study('Python'))
# print(stu3.study('Python'))


# print(stu1.get_all_attr)
# print(stu2.get_all_attr)
# print(stu3.get_all_attr)


""" 调用静态方法: 既可以用类对象调用(推荐), 也可以用实例对象调用 """
# print(Student.study('Python'))
# print(stu1.study('Python'))
# print(stu2.study('Python'))
# print(stu3.study('Python'))

""" 调用类方法: 既可以用类对象调用(推荐), 也可以用实例对象调用 """
# Student.study('Python')
# stu1.study('Python')
# stu2.study('Python')
# stu3.study('Python')

""" 调用对象方法: 既可以用实例对象调用(推荐), 也可以用类对象调用 """
# print(stu1.study('Python'))
# print(stu2.study('数学'))
# print(Student.study(stu1, 'Python'))
# print(Student.study(stu2, '数学'))


""" 访问实例属性: 只能用实例对象访问, 不能用类对象 """
# print(stu1.name)
# print(stu2.name)
# print(stu3.name)
# print(stu2.age)
# print(stu3.grade)
# print(getattr(stu1, 'name'))
# print(getattr(stu2, 'age'))
# print(getattr(stu1, 'address'))  # Error
# print(getattr(stu1, 'address', None))  # None
# print(getattr(stu1, 'age', []))  # 18

""" 访问类属性: 既可以用类对象访问(推荐), 也可以用实例对象访问 """
# print(Student.school)
# print(stu1.school)
# print(stu2.school)
# print(stu3.school)
# print(getattr(Student, 'school'))

""" 修改实例属性: 只能用实例对象修改, 不能用类对象 """
# stu1.name = '张三风'
# setattr(stu1, 'name', '张三风')
# print(stu1.name)
# print(stu2.name)
# print(stu3.name)
# stu1.age = 23
# stu1.grade = '大四'
# print(stu1.age)
# print(stu1.grade)

""" 修改类属性: 只能用类对象修改, 不能用实例对象 """
# Student.school = 'xxx培训学校'
# setattr(Student, 'school', 'xxx培训学校')
# print(Student.school)
# print(stu1.school)
# print(stu2.school)
# print(stu3.school)

""" 动态定义实例属性 """
# stu1.address = '天山路1800号'
# setattr(stu1, 'address', '天山路1800号')
# print(stu1.address)
# print(stu2.address)  # Error
# print(stu3.address)  # Error

""" 动态定义类属性 """
# Student.food = 'rice'
# setattr(Student, 'food', 'rice')
# print(Student.food)
# print(stu1.food)
# print(stu2.food)
# print(stu3.food)

""" 删除属性 """
# del stu1.age, Student.school
# delattr(stu1, 'age')
# delattr(Student, 'school')
# print(stu1.age)  # Error
# print(stu2.age)
# print(stu3.age)
# print(Student.school)  # Error
# print(stu1.school)  # Error
# print(stu2.school)  # Error
# print(stu3.school)  # Error

""" 判定属性是否存在 """
# print(hasattr(stu1, 'name'))
# print(hasattr(stu2, 'age'))
# print(hasattr(stu3, 'grade'))
# print(hasattr(Student, 'school'))
# print(hasattr(Student, 'grade'))  # False
# print(hasattr(stu1, 'address'))  # False
# print(hasattr(stu1, 'school'))
# print(hasattr(stu2, 'school'))
# print(hasattr(stu3, 'school'))
# print(getattr(stu1, 'school'))
# print(getattr(stu2, 'school'))
# print(getattr(stu3, 'school'))






# print(type(stu1) is Student)
# print(type(stu2) is Student)
# print(type(stu3) is Student)
# print(Student)



















# class Teacher:
#     pass

