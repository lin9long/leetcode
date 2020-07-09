from typing import List

class TreeNode:
    def __init__(self, x:str):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return '{}_{}_{}'.format(str(self.val),str(self.left),str(self.right))

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        # res_list = []
        # res = []

        # # root_val = root.val
        # # res.append(root_val)

        # def dfs (root):
        #     if not root : pass
        #     root_val = root.val
        #     res.append(root_val)
        #     if root.left:
        #         dfs(root.left)
        #     if root.right:
        #         dfs(root.right)
        #     # if root.left:
        #     #     dfs(root.left)
        #     # if root.right:
        #     #     dfs(root.right)

        # dfs(root)

        # res_list.append(res)
        if not root:
            return [[]]
        res = []

        def helper(root,path,res_list):
            if root.left:
                path.append(root.left)
            if root.right:
                path.append(root.right)
            if not path:
                res.append(res_list)
                return
            for i,data in enumerate(path):
                newq = path[:i] + path[i+1:]
                # helper(path[:i],res_list+)
                # + path[i+1:]
                helper(data,newq,res_list + [data.val])
            # return res
        helper(root,[],[root.val])

        return res