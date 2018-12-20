# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 11:56
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 11 在O(1)时间删除链表结点.py
# @Software: PyCharm

'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''

'''
当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个结点j的内容复制到结点i，同时把i结点的next指向j结点的next，然后再删除结点j。
如果要删除的链表为单结点链表且待删除的结点就是头结点，需要把头结点置为None，
如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点前面一个结点，然后将其next置空。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def delete_node(self, pListHead, pToBeDeleted):
        if not pListHead and pToBeDeleted:
            return None

        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext
            pNext.__del__()

        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()

        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node4 = ListNode(13)
node1.next = node2
node2.next = node3
node3.next = node4

test = Solution()
test.delete_node(node1, node3)
print(node3.val)
test.delete_node(node1, node3)
print(node3.val)
print(node2.val)
test.delete_node(node1, node1)
print(node1.val)


