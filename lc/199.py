class Solution:
    """
    199 二叉树的右视图
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        node = root
        stack = [(0,root)]
        max_depth = -1
        res = dict()
        depth = 0
        while stack :
            depth,node = stack.pop(0)
            # depth +=1
            if node :
                max_depth = max(max_depth,depth)
                res[depth] = node.val
                stack.append((depth+1,node.left))
                stack.append((depth+1,node.right))
        return [res[i] for i in range(max_depth+1)]