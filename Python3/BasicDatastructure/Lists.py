# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:59
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : Lists.py
# @Software: PyCharm

# 定义节点
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.next = newdata

    def setNext(self, nextNode):
        self.next = nextNode

temp = Node(3)
temp.setData(10)
print(temp.getNext())
print(temp.getData())

# 定义链表
class UnorderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = None
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

myList = UnorderList()
myList.add(1)
myList.add(2)
Lists = (3, 4, 5, 6, 7)
list(map(lambda x: myList.add(x), Lists))
print(myList.head.data)
print(myList.length())

print(myList.search(7))
myList.remove(5)
print(myList.add(5))
