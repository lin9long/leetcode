class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        恢复二叉搜索树
        """

        stack = []
        pred = None
        x = None
        y = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x == None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right

        tmp = y.val
        y.val = x.val
        x.val = tmp