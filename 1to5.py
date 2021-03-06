# -*- coding:utf-8 -*-

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in array:
            if target in i:
                return True  
        return False

'--------------------------------------------------------------------------------'
# 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
'--------------------------------------------------------------------------------'
# 输入一个链表，从尾到头打印链表每个节点的值。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        p = listNode
        while p:
            result.append(p.val)
            p = p.next
        return result[::-1]
'--------------------------------------------------------------------------------'
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return None
        root = pre[0]
        rootnode = TreeNode(root)
        for i in range(0, len(tin)):
            if tin[i] == root:
                break
        rootnode.left = self.reConstructBinaryTree(pre[1:1+i],tin[0:i])
        rootnode.right = self.reConstructBinaryTree(pre[1+i:],tin[i+1:])
        return rootnode
'--------------------------------------------------------------------------------'
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# -*- coding:utf-8 -*-
class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if (len(self.stack2) == 0) and (len(self.stack1) != 0):
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
            a = self.stack2[-1]
            self.stack2.pop()
            return a
        elif len(self.stack2) !=  0:
            a = self.stack2[-1]
            self.stack2.pop()
            return a