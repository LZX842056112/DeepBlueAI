"""
题目: 请设计一个学生管理系统, 包含一下内容:

1. 学生类(Student):
   - 包括属性: 学生姓名(name)、学生年龄(age)、学生成绩(score)
   - 包括功能:
     - 获取学生信息(get_info): 返回该学生的姓名、年龄和成绩。

2. 班级类(ClassRoom):
   - 包括属性: 班级名称(name)、班级学生列表(students)、所有班级列表(classes)
   - 包括功能: 
     - 添加学生(add_student): 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
     - 移除学生(remove_student): 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
     - 获取指定班级的学生信息(get_students_info): 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。

要求: 
1. 实现上述内容。
2. 编写相关测试代码。
"""


class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def __str__(self):
        return f'姓名: {self.get_name()}, 年龄: {self.get_age()}, 成绩: {self.get_score()}'

    # 获取学生信息: 返回该学生的姓名、年龄和成绩。
    def get_info(self):
        print(self)


class ClassRoom:
    classes = []

    def __init__(self, name):
        self.__students = []
        self.__name = name
        ClassRoom.classes.append(self)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def __str__(self):
        return f'班级: {self.get_name()}'

    # 获取班级信息
    def get_info(self):
        print(self)

    # 添加学生: 将学生对象添加到指定班级的学生列表中
    def add_student(self, stu):
        # 如果该学生已经在指定班级中则无需重复添加
        if stu in self.get_students():
            print(f'{stu.get_name()}已经在{self.get_name()}中，请勿重复添加!')
            return

        self.get_students().append(stu)
        # 如果该学生在其它班则调班
        for cls in ClassRoom.classes:
            if cls != self and stu in cls.get_students():
                cls.remove_student(stu)
                print(f'{stu.get_name()}之前在{cls.get_name()},现已调班!')
                break
        print(f'{stu.get_name()}成功添加到{self.get_name()}!')

    # 移除学生: 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
    def remove_student(self, stu):
        if stu in self.get_students():
            self.get_students().remove(stu)
            print(f'从{self.get_name()}中移除{stu.get_name()}!')
            return
        print(f'{stu.get_name()}不在{self.get_name()},无需移除!')

    # 获取指定班级的学生信息: 输出指定班级的所有学生信息
    @staticmethod
    def get_students_info(cls=None):
        if cls:
            cls.get_info()
            for stu in cls.get_students():
                stu.get_info()
        else:
            # 如果没有指定班级, 则默认输出所有班级的所有学生信息。
            for cls in ClassRoom.classes:
                cls.get_info()
                for stu in cls.get_students():
                    stu.get_info()


# 测试 获取学生信息(get_info)
stu1 = Student('张三', 18, 98)
stu2 = Student('李四', 20, 89)
stu3 = Student('王五', 19, 90)
stu4 = Student('赵六', 21, 95)
stu2.get_info()  # 姓名: 李四, 年龄: 20, 成绩: 89
print('*' * 40)

# 测试 班级数
cl1 = ClassRoom('1班')
cl2 = ClassRoom('2班')
cl2.get_info()  # 班级: 2班
print(len(ClassRoom.classes))  # 2
print('*' * 40)

# 测试 添加学生(add_student)
cl1.add_student(stu1)  # 张三成功添加到1班!
cl1.add_student(stu2)  # 李四成功添加到1班!
cl1.add_student(stu3)  # 王五成功添加到1班!
cl1.add_student(stu4)  # 赵六成功添加到1班!
print(len(cl1.get_students()))  # 4
# 测试 重复添加
cl1.add_student(stu1)  # 张三已经在1班中，请勿重复添加!
print(len(cl1.get_students()))  # 4
print('*' * 40)

# 测试 学生在其它班则调班
print(len(cl1.get_students()))  # 4
print(len(cl2.get_students()))  # 0
'''
从1班中移除张三!
张三之前在1班,现已调班!
张三成功添加到2班!
'''
cl2.add_student(stu1)
print(len(cl1.get_students()))  # 3
print(len(cl2.get_students()))  # 1
print('*' * 40)

# 测试 移除学生(remove_student)
cl1.remove_student(stu3) # 从1班中移除王五!
print(len(cl1.get_students()))  # 2
cl1.remove_student(stu1)  # 张三不在1班,无需移除!
print(len(cl1.get_students()))  # 2
print('*' * 40)

# 测试 获取指定班级的学生信息(get_students_info)
'''
班级: 1班
姓名: 李四, 年龄: 20, 成绩: 89
姓名: 赵六, 年龄: 21, 成绩: 95
'''
ClassRoom.get_students_info(cl1)
print('*' * 40)
'''
班级: 1班
姓名: 李四, 年龄: 20, 成绩: 89
姓名: 赵六, 年龄: 21, 成绩: 95
班级: 2班
姓名: 张三, 年龄: 18, 成绩: 98
班级: 3班
'''
ClassRoom.get_students_info()
