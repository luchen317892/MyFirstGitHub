# !/USR/BIN/ENV PYTHON3 #允许直接在Unix、Linux、Mac上运行
# -*- coding: utf-8 -*- #使用标准UTF-8编码

'我的编程记录' #文档注释，默认第一行的字符串内容

__author__ = 'Maclu'    #署名写进代码



''' 从3开始的奇数序列（生成器）

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def byname(t):
    return t[0].lower()


def byscore(t):
    return -t[1]


l1 = sorted(L, key = byscore)
print(l1)
'''

'''闭包实现计数器函数，每次调用返回递增整数
def createCounter():
    s = []
    def counter():
        s.append('a')
        return len(s)
    return counter

b = createCounter()
print(b)
print(b())
print(b())
'''

'''修饰器，使用@注入修饰器
def f1(a):
    def f2():
        print('name is :', a.__name__)
    return f2   


@f1
def now():
    print('ssss')


f = now
print(f)
print(f())
'''


"""偏函数

import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))

"""

"""构造器init

class Check4():
    # 成员方法
    def show(self):
        print("showing")

    # 构造函数
    def __init__(self, num1, s1):
        print('hello')
        # 定义成员变量，成员变量赋初始值
        self.num1 = num1
        self.s1 = s1


c4 = Check4(12, "abc")  # 12 abc
print(c4.num1, c4.s1)
"""


class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


x = Student('Alan', 88)
print(x.get_grade())
'new liefe'






