# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:18
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 15 合并两个排序的链表.py
# @Software: PyCharm

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

'''
要注意特殊输入，如果输入是空链表，不能崩溃。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, p_head1, p_head2):
        if p_head1 == None:
            return p_head2
        elif p_head2 == None:
            return p_head1

        p_merge_head = None
        if p_head1.val < p_head2.val:
            p_merge_head = p_head1
            p_merge_head.next = self.Merge(p_head1.next, p_head2)
        else:
            p_merge_head = p_head2
            p_merge_head.next = self.Merge(p_head1, p_head2.next)

        return p_merge_head

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

test = Solution()
test.Merge(node1, node4)
print(node4.next.val)

