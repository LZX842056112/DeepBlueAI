"""
Python阶段考核

说明: 总分100分, 共15道题, 其中1-8题为简答题, 9-15题为编程题, 请在每道题的注释下作答。
提交方式：还是提交到平时交作业的邮箱，抄送邮箱改为：ajiruqianlong@163.com
"""

"""
1. (3分)
Python六种标准数据类型中, 哪些类型数据是可变的? 哪些是序列? 哪些是可迭代对象? 

可变: 列表, 字典, 集合
不可变: 数字, 字符串, 元组
序列: 字符串, 列表, 元组
可迭代对象: 字符串, 列表, 元组, 字典, 集合
"""

"""
2. (2分)
在Python中, is和==的区别是什么? 

is: 判断两个对象的引用是否相等
==: 判断两个对象的值是否相等
"""

"""
3. (2分)
请问列表和元组有什么区别? 

列表: 可变; 语法为[]
元组: 不可变,没有添加/修改等方法; 语法为(),只有一个元素时后面要加','
"""

"""
4. (5分)
请描述*args和**kwargs这两个不定长参数的区别?

*args: 接收位置参数，打包成元组
**kwargs: 接收关键字参数，打包成字典，放在所有参数的最后
"""

"""
5. (5分)
请问__new__方法和__init__方法有什么区别? 

__new__: 构造方法，创建实例对象并返回
__init__: 初始化方法，定制实例对象属性，无返回值
"""

"""
6. (4分)
请描述数组和Python列表的共同点以及不同点?
 
共同点: 序列，可迭代，支持索引，支持切片
列表: 元素类型可以不同，大小可动态调整，存储对象引用
数组: 元素类型相同，固定大小，存储实际数据值
"""

"""
7. (4分)
请说明Python中break, continue, pass, return的区别? 

continue: 用于循环语句，结束当前循环，进入下一个循环
break: 用于循环语句，终止当前循环
return: 用于函数，结束函数并返回到调用方
pass: 占位作用，无操作
"""

"""
8. (5分)
闭包函数通常需要满足哪三个条件? 请定义一个闭包函数并调用它.

1.函数内部嵌套另一个函数
2.内部函数引用了外部函数的变量
3.外部函数返回内部函数
"""


def outer(x):
    def inner(y):
        return x + y

    return inner


print(outer(1)(2))

"""
9. (6分)
编写一个函数, 接受一个整数列表, 返回一个新列表, 其中包含原列表中所有偶数的平方.
"""


def square(lst):
    return [i ** 2 for i in lst if not i % 2]


print(square([1, 2, 3, 4, 5, 6]))

"""
10. (8分)
写一个正则表达式, 使得该正则表达式可以匹配[0, 9]之间的任意数字, 包括浮点数
"""

import re

p = re.compile(r'\d[\.\d]*')
print(p.findall('8axsa51c12.5as544ac'))

"""
11. (8分)
编写一个程序, 实现简单的猜数字游戏, 程序先随机生成一个1-100之间的整数, 然后用户开始猜数字,
用户输入猜测的数字, 程序给出提示(猜大了 / 猜小了 / 猜对了), 直到用户猜对该整数为止.
"""

import random

while True:
    try:
        num_user = int(input('请开始猜数字: '))
        if num_user < 1 or num_user > 100:
            raise ValueError
    except ValueError:
        print('请输入1-100之间的整数')
    else:
        num = random.randint(1, 100)
        print(f'程序生成: {num}, 用户输入: {num_user}')
        if num == num_user:
            print('猜对了')
            break
        elif num > num_user:
            print('猜小了')
        else:
            print('猜大了')

"""
12. (8分)
编写一个函数, 接收一个字符串作为参数, 以字典的形式返回字符串中的每个字符出现的次数.
"""


def number_time(string):
    tup = {}
    for i in set(string):
        tup[i] = string.count(i)
    return tup


print(number_time('fdhdgdhsjfgh'))

"""
13. (10分)
定义函数实现: 给你一个整数列表nums, 如果一组数字 (i, j) 满足nums[i] == nums[j], 且i < j,
就可以认为这是一组好数对, 返回好数对的数目.
示例:

输入: nums = [1, 2, 3, 1, 1, 3]
输出: 4
解释: 有4组好数对, 分别是(0, 3), (0, 4), (3, 4), (2, 5), 下标从0开始.
"""


def pair(lst):
    num = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] == lst[i]:
                num += 1
    return num


nums = [1, 2, 3, 1, 1, 3]
print(pair(nums))

"""
14. (10分)
定义函数实现: 给你一个字符串s, 请你返回两个相同字符之间的最长子字符串的长度, 计算长度时不含这两个字符,
如果不存在这样的子字符串, 则返回-1, 子字符串是指字符串中的一个连续字符序列.


示例 1:
输入: s = "aa"
输出: 0
解释: 最优的子字符串是两个 'a' 之间的空子字符串

示例 2:
输入: s = "abca"
输出: 2
解释: 最优的子字符串是 "bc"

示例 3:
输入: s = "cbzxy"
输出: -1
解释: s 中不存在出现出现两次的字符, 所以返回-1

示例 4:
输入: s = "cabbac"
输出: 4
解释: 最优的子字符串是 "abba", 其他的非最优解包括 "bb" 和 "".
"""

print('*' * 30)


def fun(string):
    lst = []
    for i in range(len(string)):
        rfind = string.rfind(string[i])
        if rfind != -1 and i < rfind:
            lst.append(rfind - i - 1)
    if len(lst) == 0:
        return -1
    lst.sort(reverse=True)
    return lst[0]


print(fun("ccabbadde"))
print(fun("cabbac"))
print(fun("cbzxy"))
print(fun("abca"))
print(fun("aa"))

"""
15. (20分)
设计一个图书管理系统, 包括以下几个类: 

Book类: 表示图书
包含属性: 书名(title)、作者(author)、ISBN码和出版年份(year_published)
提供方法:
__init__: 初始化图书的属性
display_info: 显示图书的详细信息


Library类: 表示图书馆
包含属性: 图书列表(books, 初始为空列表)
提供方法: 
__init__: 初始化图书馆
add_book: 向图书馆添加一本图书
remove_book: 从图书馆移除一本图书(根据ISBN码移除)
search_book: 根据书名搜索图书, 并返回所有匹配的图书列表(书名确实可以存在同名的情况)
display_books: 显示图书馆中所有图书的详细信息


Bookstore类: 继承自Library类, 表示书店
除了继承了Library的所有方法外, 当前类中还需要提供: 
sell_book: 根据ISBN码销售一本图书(从书店的图书列表中移除)
get_latest_books: 返回书店中出版年份最晚的5本图书(如果不足5本, 则返回剩下所有图书)
"""


class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return self.display_info()

    def display_info(self):
        return f'{self.title}, {self.author}, {self.isbn}, {self.year_published}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                print('添加失败，isbn重复')
                return
        self.books.append(book)
        print('添加成功')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print('删除成功')
                return True
        print('删除失败，没找到该图书')
        return False

    def search_book(self, title):
        lst = []
        for book in self.books:
            if book.title == title:
                lst.append(book)
        if len(lst) == 0:
            print('搜索失败，没找到该图书')
        return lst

    @staticmethod
    def display_books(self):
        for book in self.books:
            print(book.display_info())


class Bookstore(Library):
    @staticmethod
    def sell_book(self, isbn):
        if self.remove_book(isbn):
            print('销售成功')
            return
        print('销售失败，没找到该图书')

    @staticmethod
    def get_latest_books(self):
        lst = sorted(self.books, key=lambda book: book.year_published, reverse=True)
        length = 5
        if len(lst) < 5:
            length = len(lst)
        for i in range(length):
            print(lst[i].display_info())


book1 = Book('book1', 'author1', 'ISBN1', 1999)
book2 = Book('book2', 'author2', 'ISBN2', 1989)
book3 = Book('book3', 'author3', 'ISBN3', 1979)
book4 = Book('book4', 'author4', 'ISBN4', 2000)
book5 = Book('book5', 'author5', 'ISBN5', 1998)
book6 = Book('book6', 'author6', 'ISBN6', 1997)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.remove_book('ISBN1')
library.remove_book('ISBN4')
print(library.search_book('book3'))
print('*' * 30)

library.display_books(library)
print('*' * 30)

bookstore = Bookstore()
bookstore.get_latest_books(library)
print('*' * 30)

bookstore.sell_book(library, 'ISBN3')
bookstore.sell_book(library, 'ISBN2')
bookstore.display_books(library)
print('*' * 30)

library.display_books(library)
print('*' * 30)

bookstore.get_latest_books(library)
