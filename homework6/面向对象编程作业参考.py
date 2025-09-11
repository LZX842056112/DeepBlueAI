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
        self.name = name
        self.age = age
        self.score = score

    def get_info(self):
        return self.name, self.age, self.score


class ClassRoom:

    classes = []  # [c1, c2, c3]

    def __init__(self, name):
        self.name = name
        self.students = []
        ClassRoom.classes.append(self)

    def add_student(self, stu_obj):
        if stu_obj in self.students:
            print(f'{stu_obj.name}本来就在{self.name}, 无需重复添加!')
        else:
            for c in ClassRoom.classes:
                if stu_obj in c.students:
                    c.students.remove(stu_obj)
                    print(f'{stu_obj.name}从{c.name}离开!')
                    break
            self.students.append(stu_obj)
            print(f'{stu_obj.name}加入{self.name}!')

    def remove_student(self, stu_obj):
        if stu_obj in self.students:
            self.students.remove(stu_obj)
            print(f'{stu_obj.name}从{self.name}离开!')
        else:
            print(f'{stu_obj.name}不在{self.name}, 无需移除!')

    @staticmethod
    def get_students_info(c_obj=None):
        # c_obj = ClassRoom.classes if c_obj is None else [c_obj]
        cs = [c_obj]
        if c_obj is None:
            cs = ClassRoom.classes
        for c in cs:
            for stu in c.students:
                print(stu.get_info())


        # if c_obj is None:
        #     for c in ClassRoom.classes:  # [c1, c2, c3]
        #         for stu in c.students:
        #             print(stu.get_info())
        # else:
        #     for stu in c_obj.students:
        #         print(stu.get_info())


stu1 = Student('周一', 15, 95)
stu2 = Student('郑二', 15, 92)
stu3 = Student('张三', 16, 96)
stu4 = Student('李四', 16, 94)
stu5 = Student('王五', 17, 97)
stu6 = Student('赵六', 17, 96)
stu7 = Student('罗七', 18, 98)
stu8 = Student('吴八', 18, 99)
stu9 = Student('钱九', 19, 100)
# print(stu1.get_info())
# print(stu2.get_info())

c1 = ClassRoom('高一<3>班')
c2 = ClassRoom('高二<5>班')
c3 = ClassRoom('高三<7>班')

c1.add_student(stu1)
c1.add_student(stu2)
c2.add_student(stu3)
c2.add_student(stu4)
c2.add_student(stu5)
c3.add_student(stu6)
c3.add_student(stu7)
c3.add_student(stu8)
c3.add_student(stu9)

# c1.add_student(stu1)
# c3.add_student(stu1)

# c1.remove_student(stu2)
# c1.remove_student(stu2)

ClassRoom.get_students_info(c1)
ClassRoom.get_students_info(c2)
ClassRoom.get_students_info(c3)
ClassRoom.get_students_info()

