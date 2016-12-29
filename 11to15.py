# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n == 0:
            return 0
        if n < 0:
            n = n * (-1) - 1
            while n:
                count = count + 1
                n = n & (n-1)
            return 32-count
        else:
            while n:
            count = count + 1
                n = n & (n-1)
            return count
'-------------------------------------------------------------------'
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base ** exponent

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a = []
        b = []
        for i in array:
            if i%2==1:
                a.append(i)
            else:
                b.append(i)
        return a+b
'-------------------------------------------------------------------'
# 输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return head
        if k <= 0:
            return None
        p1 = head
        p2 = head
        for i in range(k-1):
            if p1.next:
                p1 = p1.next
            else:
                return p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2