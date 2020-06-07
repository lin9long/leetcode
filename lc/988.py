class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def smallestFromLeft(self,root:TreeNode):
        """
        二叉树字母排序最小的
        :return:
        """
        chars = []

        def dfs(root, char=[]):
            if root.left:
                dfs(root.left, char + [root.left.val])
            if root.right:
                dfs(root.right, char + [root.right.val])
            if not (root.left or root.right):
                chars.append(''.join([chr(num + ord('a')) for num in char[::-1]]))
        dfs(root, [root.val])

        return min(chars)
