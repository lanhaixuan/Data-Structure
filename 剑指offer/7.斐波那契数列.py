# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 10:42
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 7 斐波那契数列.py
# @Software: PyCharm

'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

'''
如何不使用递归实现斐波那契数列，需要把前面两个数字存入在一个数组中。
斐波那契数列的变形有很多，如青蛙跳台阶，一次跳一个或者两个；
铺瓷砖问题。变态青蛙跳，每次至少跳一个，至多跳n个，一共有f(n)=2n-1种跳法。
考察数学建模的能力。
'''

class Solution:
    # 递归解法
    def Fibonacci(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.Fibonacci(n-2) + self.Fibonacci(n-1)

    # 非递归解法
    def Fibonacci1(self, n):
        tempArray = [0, 1]
        if n == 1:
            return 1
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]


test = Solution()
print(test.Fibonacci(10))
print(test.Fibonacci(10))

