class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    """
    前序遍历还原二叉树
    """
    def recoverFromPreorder(self, S: str) -> TreeNode:
        s_l = list(S)
        depth = 0
        tree_list = defaultdict(list)
        while s_l:
            item = s_l.pop(0)
            # print(item)
            if item.isdigit():

                try:
                    pos = s_l.index('-')
                    item = [item] + s_l[:pos]
                except:
                    item = [item] + s_l

                node_item = 0
                i_l = len(item)
                for i in range(i_l):
                    node_item += int(item[i]) * 10 ** (i_l - i - 1)
                if s_l:
                    for i in range(i_l - 1):
                        s_l.pop(0)

                node = TreeNode(node_item)
                tree_list[depth].append(node)

                if depth > 0:
                    if not tree_list[depth - 1][-1].left:
                        tree_list[depth - 1][-1].left = node
                    else:
                        tree_list[depth - 1][-1].right = node

                depth = 0
            elif item == '-':
                depth += 1
                # print(depth)
        return tree_list[0][0]


if __name__ == '__main__':
    s = Solution()
    data = s.recoverFromPreorder("10-7--8")
    print(data)
