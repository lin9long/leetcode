# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    102. 二叉树的层序遍历
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        res = []
        if root: res.append([root.val])
        while q:
            level = []
            l = len(q)
            for i in range(l):
                node = q.pop(0)
                # node = q[i]
                if node:
                    if node.left:
                        level.append(node.left.val)
                        q.append(node.left)

                    if node.right:
                        level.append(node.right.val)
                        q.append(node.right)

            if level:
                res.append(level)
        return res