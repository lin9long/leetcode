class Solution:
    """
    最大二叉树
    """
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def buildTree(nums):
            if not nums :
                return
            m = max(nums)
            idx = nums.index(m)
            root = TreeNode(m)
            root.left = buildTree(nums[:idx])
            root.right = buildTree(nums[idx+1:])
            return root
        return buildTree(nums)