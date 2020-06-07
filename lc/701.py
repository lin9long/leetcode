# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    二叉搜索树的插入操作
    """
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root, val):
            # print(root.val,val)
            # if not root:
            if root.val > val:
                if root.left:
                    # if root.left.val > val:
                    insert(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    # if root.right.val < val:
                    insert(root.right, val)
                    # elif root.right.val >= val:
                    #     insert(root.left,val)
                else:
                    root.right = TreeNode(val)
            # else:
            #     root.left = TreeNode(val)

        if root:
            r_v = root.val
            if r_v > val:
                if root.left:
                    insert(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    insert(root.right, val)
                else:
                    root.right = TreeNode(val)
        else:
            root = TreeNode(val)
        return root



