from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Soluation:

    def buildTree(self, before: List[int], after: List[int]):
        """
        先序、中序还原二叉树
        :param before:
        :param after:
        :return:
        """
        # root = TreeNode(before[0])
        # before_ind = -1
        # dic = {j: i for i, j in enumerate(after)}
        # pos = dic[before[0]]
        # left = before[:pos]
        # right = before[pos + 1:]
        # def bulid(left,right,bos):

        # while before:
        #     before_ind += 1
        #     root = before.pop(0)
        #     dic_pos = dic[root]
        #     left = before[:dic_pos]
        #     right = before[dic_pos + 1:]
        # while dic_pos > before_ind:
        # print(pos, left, right)
        if after:
            root = TreeNode(before.pop(0))
            ind = after.index(root.val)
            left = after[:ind]
            right = after[ind + 1:]
            print(ind, before, left, right)
            root.left = self.buildTree(before, left)
            root.right = self.buildTree(before, right)
            return root


if __name__ == '__main__':
    before = [3,9,20,15,7]
    after = [9,3,15,20,7]
    s = Soluation()
    tree = s.buildTree(before, after)
    print(tree)
