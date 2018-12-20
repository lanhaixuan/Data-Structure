# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 9:08
# @Author  : lanhaixuan
# @Email   : jpf199727@gmail.com
# @File    : 6. 旋转数组的最小数字.py
# @Software: PyCharm

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。
如果中间点大于首元素，说明最小数字在后面一半，
如果中间点小于尾元素，说明最小数字在前一半。依次循环。
同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。
但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return
        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        minVal = rotateArray[0]
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break

            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                for i in rotateArray[front: rear+1]:
                    if rotateArray[i] < minVal:
                        minVal = rotateArray[i]
                return minVal
            elif rotateArray[midIndex] >= rotateArray[front]:
                front = midIndex
            elif rotateArray[midIndex] <= rotateArray[rear]:
                rear = midIndex
        return rotateArray[midIndex]


test = Solution()
print(test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(test.minNumberInRotateArray([4, 5, 6, 1, 2, 3]))
print(test.minNumberInRotateArray([3, 4, 5, 6, 1, 2]))





