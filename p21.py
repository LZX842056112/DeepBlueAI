class A:
    pass


class B(A, object):
    pass


class Student(object):
    pass


# Student('张三', 18, 2)
stu1 = Student()
print(stu1)
print('*' * 40)


class Student:
    school = 'xxx学校'

    def __init__(self, name, age, grade):
        print(self)
        self.name = name
        self.age = age
        self.grade = grade
        # self.school = school
        print(Student.school)
        print(locals())
        # print(school)
        print('*' * 20)

    def f(self):
        print(stu2.name)


stu1 = Student('张三', 18, 2)
stu2 = Student('李四', 20, 3)
stu3 = Student('王五', 15, 1)
print(stu1)
print(stu2)
print(stu3)
print('*' * 40)

print(Student.school)
print(stu1.school)
print(stu2.school)
print(stu3.school)
print('*' * 40)

stu1.f()
stu2.f()
stu3.f()
print('*' * 40)
print('*' * 40)

print(getattr(Student, 'school'))
print(getattr(stu1, 'name'))
print(getattr(stu1, 'address', None))
print('*' * 40)

stu1.school = '2222222'
print(Student.school)
print(stu1.school)
print(stu2.school)
print(stu3.school)
print('*' * 40)

Student.qwe = 'zzz'
print(Student.qwe)
print(stu1.qwe)
print(stu2.qwe)
stu2.qwe = 'qwe'
print(stu2.qwe)
print(stu1.qwe)
print(stu3.qwe)
print('*' * 40)

setattr(stu1, 'id', 123)
print(stu1.id)
print(hasattr(stu1, 'id'))
print(hasattr(stu2, 'id'))
print(hasattr(Student, 'id'))
print('*' * 40)

setattr(Student, 'zxc', 123)
print(hasattr(Student, 'zxc'))
print(hasattr(stu1, 'zxc'))
print('*' * 40)

del stu1.id, Student.qwe
print(hasattr(stu1, 'id'))
print(hasattr(stu2, 'id'))
print(hasattr(Student, 'id'))
print(hasattr(Student, 'qwe'))
print('*' * 40)

delattr(Student, 'zxc')
print(hasattr(stu2, 'zxc'))
