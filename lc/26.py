class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    判斷是否為子樹
    """

    def isSubTree(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val != b.val:
            return False
        return self.isSubTree(a.left, b.left) and self.isSubTree(a.right, b.right)

    def isSubStructure(self, A, B):
        result = False
        if A and B:
            result = self.isSubTree(A, B)
        if not result and A.left:
            result = self.isSubStructure(A.left, B)
        if not result and A.right:
            result = self.isSubStructure(A.right, B)
        return result
