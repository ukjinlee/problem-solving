class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        
class Tree:
    def __init__(self):
        self.root = None
        
    def add_node(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root.children.append(TreeNode(val))
