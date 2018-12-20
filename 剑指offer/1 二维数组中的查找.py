# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 20:37
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 1二维数组中的查找.py
# @Software: PyCharm

'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
'''

class Solution:
    def Find(self, array, target):
        # 判断数组是否为空
        if array is None:
            return False

        rawnum = len(array)
        colnum = len(array[0])

        i = colnum - 1
        j = 0
        while i >= 0 and j < rawnum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False

    # 输出数组中 target 的个数
    def searchMatrix(self, matrix, target):
        if matrix is None:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols-1
        count = 0
        while row <= rows-1 and col >=0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                count += 1
                col -= 1
        return count

array = [
    [1, 2, 3, 4],
    [2, 3, 5, 6],
    [5, 7, 8, 9],
    [8, 9, 10, 11]
]

findTarget = Solution()
print(findTarget.Find(array, 8))
print(findTarget.searchMatrix(array, 8))




