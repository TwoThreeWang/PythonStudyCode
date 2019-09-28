#!/usr/bin/env python
# encoding: utf-8

"""
@version: python 3.7
@author: wangcheng
@software: PyCharm
@file: namedTuple.py
@time: 2019-09-28 16:00
@contact: namedtuple 学习代码
"""
from collections import namedtuple


def printTitle(title):
    # 打印分隔标题
    print(f' {title} '.center(50, '-'))


def begin():
    # tuple 拆包
    printTitle('tuple 拆包')
    user_tuple = ('wangcheng', 23, 170, 'beijing')
    name, age, height, local = user_tuple
    print(name, age, height, local)  # wangcheng 23 170 beijing
    name, *others = user_tuple
    print(name, others)  # wangcheng [23, 170, 'beijing']

    # namedtuple
    # 使用 namedtuple 比使用类节省内存
    printTitle('namedtuple')
    User = namedtuple("User", ["name", "age", "height"])
    user = User('wangcheng', 23, 170)
    print(user.name, user.age, user.height)  # wangcheng 23 170
    user2 = User('wang', 20, 180)
    print(user2.name, user2.age, user2.height)  # wang 20 180
    print(user)  # User(name='wangcheng', age=23, height=170)
    # namedtuple 跟 tuple 一样支持拆包
    name, age, *other = user
    print(name, age, other)  # wangcheng 23 [170]

    # tuple 映射到 namedtuple
    printTitle('tuple 映射到 namedtuple')
    User = namedtuple('User', ['name', 'age'])
    user_tuple = ('cheng', 23)
    user = User(*user_tuple)
    print(user)

    printTitle('tuple 映射到 namedtuple 补充字段')
    User = namedtuple('User', ['name', 'age', 'height'])
    user_tuple = ('cheng', 23)  # tuple 比 User 少一个字段
    user = User(*user_tuple, '173')  # 可在后补充缺失字段
    print(user)
    user = User(*user_tuple, height='177')  # 指定补充字段的key
    print(user)
    user = User('173', *user_tuple)  # 也可在前补充缺失字段
    print(user)
    user_dict = {
        "name": "wangcheng",
        "age": 23,
        "height": 170
    }
    user = User(**user_dict)
    print(user)
    user_list = ['cheng', 23, 170]  # 列表也是可以的
    user = User(*user_list)
    print(user)
    # 转化为 dict
    user_info_dict = user._asdict()
    print(user_info_dict)  # OrderedDict([('name', 'cheng'), ('age', 23), ('height', 170)])


# 拓展：函数参数 *args 和 **kwargs
def ask(*args, **kwargs):
    print(f'args = {args}, kwargs = {kwargs}')


if __name__ == '__main__':
    begin()
    ask("wangcheng", 29)  # args = ('wangcheng', 29), kwargs = {}
    ask(name="wangcheng", age=29)  # args = (), kwargs = {'name': 'wangcheng', 'age': 29}
