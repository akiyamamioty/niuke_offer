# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.flag = []
    def push(self, node):
        self.stack.append(node)
        if (len(self.flag)==0) or (node<self.flag[-1]):
            self.flag.append(node)
        else:
            self.flag.append(self.flag[-1])
    def pop(self):
        self.stack.pop()
        return self.flag.pop()
    def top(self):
            return self.stack[-1]
    def min(self):
        if len(self.flag):
            return self.flag[-1]
        else:
            return 