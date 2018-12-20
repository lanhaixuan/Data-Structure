# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 8:45
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 14 反转链表.py
# @Software: PyCharm

'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

'''
需要注意三个问题：输入的链表头指针为None或者整个链表只有一个结点时，反转后的链表出现断裂，返回的翻转之后的头节点不是原始链表的尾结点。
因此需要引入一个翻转后的头结点，以及一个指向当前结点的指针，一个指向当前结点前一个结点的指针，一个指向当前结点后一个结点的指针，防止出现断裂。
推广：递归实现反转链表
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, pHead):
        pReverseHead = None
        pNode = pHead
        pPreNode = None

        while pNode != None:
            pNext = pNode.next

            if pNext == None:
                pReverseHead = pNode

            pNode.next = pPreNode
            pPreNode = pNode
            pNode = pNext

        return pReverseHead

    def reverse_list_rec(self, head):
        if not head or not head.next:
            return head
        else:
            pReverseHead = self.reverse_list_rec(head.next)
            head.next.next = head
            head.next = None
            return pReverseHead


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

test = Solution()
# print(test.reverse_list(node1).next.val)
print(test.reverse_list_rec(node1).val)



