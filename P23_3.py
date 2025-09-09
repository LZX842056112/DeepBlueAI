class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.show()

    def get_up(self):
        print(f'{self.name}睁开眼睛')
        print(f'{self.name}起身')
        print(f'{self.name}穿好衣服')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def sleep(self):
        print(f'{self.name}脱掉外套')
        print(f'{self.name}躺下')
        print(f'{self.name}闭上眼睛')


class Student(Person):
    count_s = 0

    def __init__(self, name, age, grade):
        self.grade = grade
        super().__init__(name, age)
        Student.count_s += 1

    def show(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 目前正在读{self.grade}!')

    def login_id(self):
        print(f'{self.name}输入账号密码')
        print(f'{self.name}登陆账号成功')

    def study(self):
        print(f'{self.name}看视频')
        print(f'{self.name}查资料')
        print(f'{self.name}写代码')

    @staticmethod
    def publish():
        print(f'当前学生人数: {Student.count_s}')


class Teacher(Person):
    count_t = 0

    def __init__(self, name, age, department):
        self.department = department
        super().__init__(name, age)
        Teacher.count_t += 1

    def show(self):
        print(f'大家好! 我是{self.name}, 今年{self.age}岁, 在{self.department}任职!')

    def clock_in(self):
        print(f'{self.name}录入指纹')
        print(f'{self.name}打卡成功')

    def work(self):
        print(f'{self.name}授课')
        print(f'{self.name}答疑')
        print(f'{self.name}写代码')

    @staticmethod
    def publish():
        print(f'当前老师人数: {Teacher.count_t}')


stu1 = Student('张三', 18, '大二')
stu2 = Student('李四', 20, '大一')
stu3 = Student('王五', 19, '大一')
stu1.get_up()
stu1.sleep()
stu2.wash()
stu3.eat()

tea1 = Teacher('老李', 45, '财务部')
tea2 = Teacher('老刘', 50, '教务部')
tea1.clock_in()
tea2.work()
Student.publish()
Teacher.publish()
