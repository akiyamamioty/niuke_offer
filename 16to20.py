# -*- coding:utf-8 -*-
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pNode1 = pHead1
        pNode2 = pHead2
        if pNode1.val <= pNode2.val:
            pNode = pNode1
            pNode1 = pNode1.next
        else:
            pNode = pNode2
            pNode2 = pNode2.next
        pHead = pNode
        while pNode1 or pNode2:
            if not pNode1:
                pNode.next = pNode2
                pNode2 = pNode2.next
            elif not pNode2:
                pNode.next = pNode1
                pNode1 = pNode1.next
            else:
                if pNode1.val <= pNode2.val:
                    pNode.next = pNode1
                    pNode1 = pNode1.next
                else:
                    pNode.next = pNode2
                    pNode2 = pNode2.next
            pNode = pNode.next
        return pHead