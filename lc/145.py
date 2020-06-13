class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Soluation:

    def postorderTreveral(self, root: TreeNode):

        res = []
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left if node.left is not None else node.right
            node = stack.pop()
            res.append(node.val)
            if stack and stack[-1].left == node:
                node = stack[-1].right
            else:
                node = None
        return res

if __name__ == '__main__':
    s = Soluation()
    root = TreeNode(1)
    # root.left = None
    right = TreeNode(2)
    right.left = TreeNode(3)
    root.right = right

    print(s.postorderTreveral(root))

