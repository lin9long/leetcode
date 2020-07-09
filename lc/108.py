
from typing import List

class TreeNode:
    def __init__(self, x:str):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return '{}_{}_{}'.format(str(self.val),str(self.left),str(self.right))


class Soluation:
    """
    重构二叉树
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        nums = sorted(nums)
        nums_len = len(nums)
        left = 0
        right = nums_len - 1

        def bulidTree(left,right):
            if left > right:
                return None
            mid = (right + left) // 2
            root = TreeNode(nums[mid])
            root.left = bulidTree(left, mid - 1)
            root.right = bulidTree(mid+1,right)
            return root
        return bulidTree(left,right)



if __name__ == '__main__':
    list_data = [-3,1,0,5,6,7]
    s = Soluation()
    tree = s.sortedArrayToBST(list_data)
    print(tree)