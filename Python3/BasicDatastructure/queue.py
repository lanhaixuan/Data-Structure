# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 18:46
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : queue.py
# @Software: PyCharm

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return