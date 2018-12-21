# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:02
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 8 二进制中1的个数.py
# @Software: PyCharm

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

'''
注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个，
因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1。
注意：书中给了另外两种方法，分别是原始n左移一位和右移一位的方法，因为Python不会出现整数溢出的情况，这里就不再考虑着两种方法。
扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0。
或者求两个整数m和n需要改变m二进制中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。
'''


class Solution:
    def Numberof1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1) & n
        return count

    def Numberof2(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')

test = Solution()
print(test.Numberof1(10))
print(test.Numberof1(-10))
print(test.Numberof2(10))
print(test.Numberof2(-10))
