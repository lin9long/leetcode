# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self,root: TreeNode):
        if not root:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        tmp = max(root.val, root.val + l, root.val + r)
        self.res = max(tmp, self.res, root.val + r + l)
        return tmp

