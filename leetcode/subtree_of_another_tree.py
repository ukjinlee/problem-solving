# 572. Subtree of Another Tree
# 
# Given two non-empty binary trees s and t, 
# check whether tree t has exactly the same structure and node values with a subtree of s. 
# A subtree of s is a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s, t) -> bool:
        return self.dfsFunc(s, t)
        
    def dfsFunc(self, s, t) -> bool:
        if s is None:
            return False
            
        if self.compareTree(s, t):
            return True
        if dfsFunc(s.left, t):
            return True
        return dfsFunc(s.right, t)
        
    def compareTree(self, t1, t2) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None:
            return False
        if t2 is None:
            return False
        return t1.val == t2.val and self.compareTree(t1.left, t2.left) and self.compareTree(t1.right, t2.right)
