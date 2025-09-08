class Student:
    __school = 'xxx学校'

    def __init__(self, name, age, grade):
        self.__name = name
        self.age = age
        self.grade = grade

    # def study(self, course):
    #     return f'{self.name}在听{course}课'

    def study(self, course):
        return f'{self.__name}在听{course}课'

    # @staticmethod
    # def study(course):
    #     print('staticmethod')
    #     return f'{Student.school}的学生在听{course}课'
    #
    # @classmethod
    # def study(self, course):
    #     print('classmethod')
    #     return f'{self.school}的学生在听{course}课'

    @classmethod
    def study2(x, course):
        print('classmethod')
        return f'{x.__school}的学生在听{course}课'

    @staticmethod
    def study3(course):
        print('staticmethod')
        return f'{Student.__school}的学生在听{course}课'


    def get_all_attr2(self):
        return f'{self.__name}在听课'

    @property
    def get_all_attr(self):
        return f'{self.__name}在听课'

    def __study1(self, course):
        return f'{self.__name}在听{course}课'

    def call_study1(self, course):
        return self.__study1(course)

    @classmethod
    def __study3(cls, course):
        print(f'{cls.__school}的学生在听{course}课')
        print(f'{Student.__school}的学生在听{course}课')

    def call_study3(cls, course):
        return cls.__study3(course)


stu1 = Student('张三', 18, 2)
stu2 = Student('李四', 20, 3)
stu3 = Student('王五', 15, 1)

print(stu1.study('python'))
stu1.__init__('张三丰', 20, 0)
print(Student.study(stu1, 'python'))
print('*' * 40)

print(stu1.study2('Python'))
print(stu2.study2('Python'))
print('*' * 40)

print(Student.study3('Python'))
print(stu1.study3('Python'))
print('*' * 40)

# print(Student.study('Python'))
# print(stu1.study('Python'))
print(stu1.get_all_attr2())
print('*' * 40)

print(Student.get_all_attr)
print(stu1.get_all_attr)
print('*' * 40)

print(stu1.call_study1('python'))
print('*' * 40)

stu1.call_study3('python')
print('*' * 40)
print('*' * 40)
