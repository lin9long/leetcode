# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        排序链表、快速排序
        :param head:
        :return:
        """

        # def switch(start,end):
        #     cur,nex = start,start.next
        #     tmp = end.next
        #     end.next = start
        #     # start = end
        #     start.next = tmp
        #     return end

        # first = head.val
        # while head:
        #     cur = head.val
        #     head = head.next

        if not head:
            return head

        big = None
        small = None
        equal = None
        cur = head
        while cur:
            t = cur
            cur = cur.next
            if t.val > head.val:
                t.next = big
                big = t
            elif t.val < head.val:
                t.next = small
                small = t
            else:
                t.next = equal
                equal = t

        big = self.sortList(big)
        small = self.sortList(small)

        ret = ListNode(None)
        pos = ret

        for p in [small, equal, big]:
            while p:
                pos.next = p
                p = p.next
                pos = pos.next
                pos.next = None
        return ret.next
