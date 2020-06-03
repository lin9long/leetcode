class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head_pointer = root
        while head_pointer:
            cur = head_pointer
            pre = head_pointer = None
            while cur :
                if cur.left:
                    if not pre:
                        pre = head_pointer = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head_pointer = cur.right
                    else:
                        pre.next  = cur.right
                        pre = pre.next
                cur = cur.next
        return root
