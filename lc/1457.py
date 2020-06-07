class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """
        判断是否为伪回文
        :param root:
        :return:
        """
        self.a = [0] * 10
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return
        self.a[root.val] += 1
        if not root.left and not root.right:
            md = 0
            for i in range(10):
                if self.a[i] % 2 != 0 and self.a[i] != 0:
                    md += 1
            if md < 2:
                self.count += 1

        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
        self.a[root.val] -= 1
