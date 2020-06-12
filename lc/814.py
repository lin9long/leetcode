# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if not root: return 0
            # if not root.left and not root.right and root.val == 0:
            #     root = None
            # return
            if dfs(root.left) == 0: root.left = None
            if dfs(root.right) == 0: root.right = None
            return dfs(root.left) or dfs(root.right) or root.val

        dfs(root)
        return root
