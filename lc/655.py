# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    输出二叉树
    """
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # left = []
        # right = []
        # def dfs(root,depth):
        #     if root.left or root.right:
        #         depth += 1
        #         if root.left:
        #             left.append(root.left.val)
        #             dfs(root.left,depth)

        #         if root.right:
        #             right.append(root.right.val)
        #             dfs(root.right,depth)
        #     return depth

        # depth = max(dfs(root.left,1),dfs(root.right,1))
        # print(depth,left,right)
        # tmp = 0
        # for i in range(depth):
        #     tmp = tmp * 2 +1
        # tree = [ [''] * (tmp*2 +1) for i in range(depth)]
        # print(tree)
        def getHight(root):
            if not root:
                return 0
            return 1 + max(getHight(root.left), getHight(root.right))

        hight = getHight(root)
        n = 2 ** hight - 1
        tree = [n * [""] for i in range(hight)]
        root_list = []

        def dfs(root, depth, index):
            if not root: return
            root_list.append((root.val, depth, index))
            dfs(root.left, depth + 1, 2 * index)
            dfs(root.right, depth + 1, 2 * index + 1)

        dfs(root, 0, 0)
        print(root_list, tree)
        for v, d, i in root_list:
            ind = int((2 ** (hight - d - 1)) * (2 * i + 1) - 1)
            tree[d][ind] = str(v)
        return tree






