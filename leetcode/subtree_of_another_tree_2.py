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
    def isSubtree(self, s, t):
        sList = []
        self.buildTreeList(s, sList)        
        sStr = ','.join(sList)
        tList = []
        self.buildTreeList(t, tList)        
        tStr = ','.join(tList)
        return tStr in sStr
    
    def buildTreeList(self, node, nodeList):
        if node is None:
            nodeList.append('null')
            return
        
        nodeList.append("[" + str(node.val) + "]")
        self.buildTreeList(node.left, nodeList)
        self.buildTreeList(node.right, nodeList)
