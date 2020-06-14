class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_node(self, val):
        self.children.append(TreeNode(val))


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root.children.append(TreeNode(val))

    def dfs_recursive(self, node=None):
        if (node is None):
            node = self.root

        print("%d ->" % node.val, end=" ")
        for child in node.children:
            self.dfs_recursive(child)
        if node is self.root:
            print('end')

    def dfs_stack(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print("%d ->" % node.val, end=" ")
            stack += reversed(node.children)
        print('end')

    def bfs(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print("%d ->" % node.val, end=" ")
            queue += node.children
        print('end')


def test():
    tree = Tree()

    val = 1
    tree.add_node(val)
    val += 1

    for i in range(3):
        tree.add_node(val)
        val += 1

    for child in tree.root.children:
        for i in range(2):
            child.add_node(val)
            val += 1

    tree.dfs_recursive()
    tree.dfs_stack()
    tree.bfs()


if __name__ == "__main__":
    test()
