class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1:
            return not t2
        if not t2:
            return True
        else:
            return self.dfs(t1,t2) or self.checkSubTree(t1.left,t2) or self.checkSubTree(t1.right,t2)


    def dfs(self,t1,t2):
        if not t1:
            return not t2
        elif not t2:
            return True
        elif t1.val != t2.val:
            return False

        return self.dfs(t1.left,t2.left) and self.dfs(t1.right,t2.right)