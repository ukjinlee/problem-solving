class BinaryTreeNode:
    def __init__(self, value):
        self.value = value  # int
        self.left = None  # BinaryTreeNode
        self.right = None  # BinaryTreeNode

    def add_node(self, value):
        if self.value < value:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = BinaryTreeNode(value)
        else:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = BinaryTreeNode(value)

    def traverse(self, node):
        if not node:
            return
        q = [node]

        print(f"%d->{node.value}", end="")
        self.traverse(node.left)
        self.traverse(node.right)

    def search(self, value, count):
        if self.value == value:
            return True, count
        if self.value < value:
            return self.right.search(value, count + 1) if self.right is not None else (False, count)
        return self.left.search(value, count + 1) if self.left is not None else (False, count)


class BinaryTree:
    def __init__(self, value):
        self.root = BinaryTreeNode(value)

    def add_node(self, value):
        self.root.add_node(value)

    def print(self):
        q = [{
            "node": self.root,
            "depth": 0
        }]
        current_depth = 0
        while q:
            n = q.pop(0)
            node = n["node"]
            if n["depth"] != current_depth:
                current_depth += 1
                print()

            if node:
                print(str(node.value), end=", ")
                q.append({
                    "node": node.left,
                    "depth": current_depth + 1
                })
                q.append({
                    "node": node.right,
                    "depth": current_depth + 1
                })

    def search(self, value):
        return self.root.search(value, 1)


def test():
    tree = BinaryTree(5)
    tree.add_node(3)
    tree.add_node(2)
    tree.add_node(4)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(6)
    tree.add_node(10)
    tree.add_node(9)
    tree.print()
    found, count = tree.search(6)
    if found:
        print(f"Found 6; count is {count}")
    else:
        print(f"Not found 6; count is {count}")
    found, count = tree.search(11)
    if found:
        print(f"Found 11; count is {count}")
    else:
        print(f"Not found 11; count is {count}")


if __name__ == '__main__':
    test()
