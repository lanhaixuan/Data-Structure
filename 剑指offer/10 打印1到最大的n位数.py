# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:32
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 10 打印1到最大的n位数.py
# @Software: PyCharm

'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

'''
该题的要点是注意输入的n位数是否会导致溢出，因此利用字符串模拟整数的加法。
注意：在打印函数中，需要判断打印的数字是否是以0开头的，同时判断条件是 num[i] != "0"，
不能写作 num[i] != 0，因为是使用str类型的，后面一种写法导致判断无法成功。
'''


def Print1ToMaxofNdigits1(n):
    if n <= 0:
        return
    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxofNDigitsRecursively(number, n, 0)


def Print1ToMaxofNDigitsRecursively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return

    for i in range(10):
        number[index + 1] = str(i)
        Print1ToMaxofNDigitsRecursively(number, length, index+1)

def PrintNumber(number):
    isBegining0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBegining0 and number[i] != '0':
            isBegining0 = False
        if not isBegining0:
            print('{0}'.format(number[i]), end='')
    print('')


Print1ToMaxofNdigits1(2)
