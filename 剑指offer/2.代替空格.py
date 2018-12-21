# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 21:04
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 2 代替空格.py
# @Software: PyCharm

'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
如果直接每次遇到空格添加'%20'，那么空格后面的数字就需要频繁向后移动。
遇到这种移动问题，我们可以尝试先给出最终需要的长度，然后从后向前扫描，同时给定两个指针来保证定位。
'''

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        string = list(s)
        stringReplace = []
        for item in string:
            if item == ' ':
                stringReplace.append('%20')
            else:
                stringReplace.append(item)
        return ''.join(stringReplace)

    # 简单代码替换
    # 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
    def replaceSpace1(self, s):
        if not isinstance(s, str):
            return
        return s.replace(' ', '%20')


s = 'We Are Happy'
test = Solution()
print(test.replaceSpace(s))
print(test.replaceSpace1(s))
