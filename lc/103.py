# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    103. 二叉树的锯齿形层次遍历
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict

        if not root: return []
        stack = [(1, root)]
        depth = 1
        dic = defaultdict(list)
        while stack:
            depth, node = stack.pop()
            dic[depth].append(node.val)
            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))

        return [v[::-1] if k % 2 != 0 else v for k, v in dic.items()]


