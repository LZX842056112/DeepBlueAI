class Animal:
    name = '动物'

    @staticmethod
    def cute():
        print('动物卖萌')


class Cat(Animal):
    name = '猫'

    @staticmethod
    def cute():
        print('猫卖萌')


class Ragdoll(Cat):
    name = '布偶猫'

    @staticmethod
    def cute():
        print('布偶猫卖萌')


Ragdoll.cute()
super(Ragdoll, Ragdoll).cute()
super(Cat, Ragdoll).cute()

Cat.cute()
super(Cat, Cat).cute()

print(Ragdoll.name)
print(super(Ragdoll, Ragdoll).name)
print(super(Cat, Ragdoll).name)
print(super(Cat, Cat).name)
print('*' * 40)


class Animal:
    def cute(self):
        print('动物卖萌')


class Cat:
    def cute(self):
        print('猫卖萌')


class Ragdoll(Cat, Animal):
    def cute(self):
        print('布偶猫卖萌')

    def cute2(self):
        print('布偶猫卖萌')
        super().cute()
        super(Ragdoll, self).cute()
        super(Cat, self).cute()


class Exam(Animal):
    def cute(self):
        print('Exam卖萌')


r = Ragdoll()
r.cute()
super(Ragdoll, r).cute()
super(Cat, r).cute()
print('*' * 40)

# super(Exam, r).cute()
r.cute2()
