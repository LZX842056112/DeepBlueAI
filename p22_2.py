class Person:
    state = "China"

    @staticmethod
    def eat():
        print('吃饭')

    @staticmethod
    def speak():
        print('说话')


class Student(Person):
    @staticmethod
    def study():
        print('读书')


class Worker(Person):

    @staticmethod
    def work():
        print('搬砖')


print(Worker.state)
Worker.work()
Worker.eat()
Worker.speak()
print('*' * 40)

print(Student.state)
Student.eat()
Student.speak()
# Student.work()
print('*' * 40)
print('*' * 40)


class Animal:
    name = '动物'

    def __init__(self, who, food):
        self.food = food
        self.who = who

    @staticmethod
    def cute():
        print('动物卖萌')

    # def eat(self, who):
    #     print(f'{who}吃{self.food}')
    def eat(self):
        print(f'{self.who}吃{self.food}')


class Cat(Animal):
    # pass
    name = '猫'

    @staticmethod
    def cute():
        print('猫卖萌')

    @staticmethod
    def catch_mouse():
        print('猫抓老鼠')


class Ragdoll(Cat, Animal):
    @staticmethod
    def cute():
        print('布偶猫卖萌')


class Dog(Animal):
    # pass
    name = '狗'

    def eat(self):
        print(f'狗吃{self.food}')


Ragdoll.cute()
print('*' * 40)

Ragdoll.cute()
Ragdoll.catch_mouse()
# Ragdoll.eat()
print('*' * 40)

# a = Animal('🥩')
# print(a.food)
#
# d = Dog('🍎')
# print(d.food)
#
# c = Cat('🐟')
# print(c.food)
print('*' * 40)

# a.eat('动物')
# d.eat('猫')
# c.eat('狗')
print('*' * 40)

Animal('动物', '🥩').eat()
Cat('猫', '🍎').eat()
Dog('狗', '🐟').eat()
print('*' * 40)

print(Animal.name)
print(Cat.name)
print(Dog.name)
