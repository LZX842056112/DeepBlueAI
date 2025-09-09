class A:
    def __init__(self, name):
        self.name = name
        self.Q()

    def Q(self):
        print(self.name, 'Q方法被调用')


class B(A):
    pass


b = B('张三')
b.Q()
print('*' * 40)


class C(A):
    def __init__(self, name):
        self.name = name


c = C('赵六')
c.Q()
print('*' * 40)


class D(A):
    def __init__(self, name):
        super(D, self).__init__('李四')
        self.name = name


d = D('王五')
d.Q()
print('*' * 40)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


a, b, c = A(), B(), C()
print(type(a) is A)  # True
print(type(b) is A)  # False，type不考虑继承
print(type(c) is A)  # False，type不考虑继承
print(isinstance(a, A))  # True
print(isinstance(b, A))  # True，考虑继承
print(isinstance(c, A))  # True，考虑继承
print(isinstance(c, (B, A)))  # True，c是A子类的实例
print(isinstance(a, (B, C)))
print('*' * 40)


class C(B):
    pass


print(issubclass(B, A))  # True
print(issubclass(C, A))  # True
print(issubclass(A, A))  # True，类会被视作其自身的子类
print(issubclass(C, (B, A)))  # True
print(issubclass(A, (B, C)))
print('*' * 40)


class Apple:
    @staticmethod
    def change():
        return '啊~ 我变成了苹果汁!'


class Banana:
    @staticmethod
    def change():
        return '啊~ 我变成了香蕉汁!'


class Mango:
    @staticmethod
    def change():
        return '啊~ 我变成了芒果汁!'


class Juicer:
    @staticmethod
    def work(fruit):
        print(fruit.change())


"""
三个内容不同的change方法使用相同的名字命名,
只要改变change的调用对象, 就可以调用不同内容的方法
"""
Juicer.work(Apple)
Juicer.work(Banana)
Juicer.work(Mango)
