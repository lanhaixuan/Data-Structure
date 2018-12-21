# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 21:23
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 3 从头到尾打印列表.py
# @Software: PyCharm

'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

'''
从头到尾遍历链表，并用一个栈存储每个结点的值，之后出栈输出值即可。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode.val is None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

test = Solution()
print(test.printListFromTailToHead(node1))
