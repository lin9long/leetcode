class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Soluation:
    """
    中序遍历二叉树
    """

    def inorderTreveral(self, root: TreeNode):
        if not root: return []
        res = []
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res
