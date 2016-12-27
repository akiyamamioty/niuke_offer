# -*- coding:utf-8 -*-

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        else:
            return min(rotateArray)

'------------------------------------------------------'
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a = 1
        b = 1
        c = 0
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n > 1:
            for i in range(0,n-2):
                c = a + b
                a = b
                b = c
            return c
'------------------------------------------------------'
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 2
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number > 2:
            for i in range(number-2):
                c = a+b
                a = b
                b = c
            return c
'------------------------------------------------------'
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        result = 0
        a = 1
        b = 2
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number > 2:
            for i in range(1,number-1):
                result = result + self.jumpFloorII(number-i)
            result = result+1
            return result+1
'------------------------------------------------------'
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        a = 1
        b = 2
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 2
        while number > 2:
            b = b + a
            a = b - a 
            number -= 1
        return b

