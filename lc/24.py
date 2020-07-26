# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    24. 两两交换链表中的节点
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(n1,n2):
            n2.next = n1
            # n1.next = None
            # n2 = n2.next
            return n2
        c = 0
        n1 = None
        n2 = None
        res = []
        if not head : return head
        if not head.next : return head
        while head:
            if c == 0 :
                n1 = ListNode(head.val)
            if c == 1 :
                n2 = ListNode(head.val)
            if c == 1 :
                c = 0
                # print(n1,n2)
                res.append(helper(n1,n2))
                n1,n2 = None,None
            else:
                c+=1
            head = head.next
        print(res)
        ret = ListNode(None)
        tmp = ret
        while res:
            node = res.pop(0)
            tmp.next = node
            tmp = tmp.next.next
        if n1:
            tmp.next = n1
        if n2:
            tmp.next = n2
        return ret.next




