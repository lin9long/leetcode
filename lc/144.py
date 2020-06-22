class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Soluation:
    """
    前续遍历二叉树
    """

    def preorderTreveral(self, root: TreeNode):

        if not root :return []
        res = []
        node = root
        stack = [root]
        while stack:
            # while node:
            #     node = node.left if node.left is not None else node.right
            #     stack.append(node)
            node = stack.pop()
            res.append(node.val)
            if node.right :
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

