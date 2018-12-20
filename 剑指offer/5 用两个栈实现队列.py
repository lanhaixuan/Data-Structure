# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 8:53
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 5 用两个栈实现队列.py
# @Software: PyCharm

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
需要两个栈Stack1和Stack2，push的时候直接push进Stack1。
pop需要判断Stack1和Stack2中元素的情况，Stack1空的话，直接从Stack2 pop，Stack1不空的话，把Stack1的元素push进入Stack2，然后pop Stack2的值。
'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


test = Solution()
test.push(1)
test.push(2)
test.push(3)
print(test.pop())
test.push(4)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())

