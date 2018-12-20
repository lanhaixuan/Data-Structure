# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:16
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 12 调整数组顺序使奇数位于偶数前面.py
# @Software: PyCharm

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
注重函数的扩展性能。把函数中的判断条件写成一个判断条件的函数，方便与函数的扩展。
对于奇数位于偶数前面的情况，类似于快排，在头和尾分别设置一个指针，头指针指向奇数则后移，尾指针指向偶数则前移。
'''


class Solution:
    # 快排思想，满足了奇数在前，偶数在后，但是奇偶的相对顺序改变
    def reorder_array(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front, rear = 0, len(array) - 1
        while front <= rear:
            while array[rear] % 2 == 0:
                rear -= 1
            while array[front] % 2 == 1:
                front += 1
            array[front], array[rear] = array[rear], array[front]
        return array

    def reorder_array2(self, array):
        left = [i for i in array if i%2]
        right = [i for i in array if not i%2]
        return left + right


test = Solution()
print(test.reorder_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(test.reorder_array2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
