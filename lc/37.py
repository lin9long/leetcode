class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    二叉树序列化
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop(0)
            if tmp:
                res.append(str(tmp.val))
                stack.append(tmp.left)
                stack.append(tmp.right)
            else:
                res.append('null')
        # print(res)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return []
        sp_data = data.split(',')
        idx = 1
        root = TreeNode(sp_data[0])
        stack = [root]
        while stack:
            tmp = sp_data[idx]
            node = stack.pop(0)
            if tmp != 'null':
                node.left = TreeNode(int(tmp))
                stack.append(node.left)
            idx += 1
            tmp = sp_data[idx]
            if tmp != 'null':
                node.right = TreeNode(int(tmp))
                stack.append(node.right)
            idx += 1
        return root
