#!/usr/bin/python
# -*-coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    """

    # def isValidBST(self, root: TreeNode) -> bool:
    #     n_l, target = [], float('-inf')
    #     while n_l or root:
    #         while root:
    #             n_l.append(root)
    #             root = root.left
    #         root = n_l.pop()
    #         if root.val <= target:
    #             return False
    #         target = root.val
    #         root = root.right
    #     return True
    target = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.target:
            return False
        self.target = root.val
        root = root.right
        return self.isValidBST(root)


if __name__ == '__main__':
    t1 = TreeNode(10)
    t1.left = TreeNode(11)
    t1.right = TreeNode(14)

    s = Solution()
    res = s.isValidBST(t1)
    print(res)
