

class Solution:
    """
    . 合并两个有序链表
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        解法一
        :param l1:
        :param l2:
        :return:
        """
        import heapq
        res = []
        res_l = tmp_res = ListNode(None)
        while l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            if l1 :
                heapq.heappush(res, l1_v)
            if l2:
                heapq.heappush(res, l2_v)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        while res:
            tmp_res.next = ListNode(heapq.heappop(res))
            tmp_res = tmp_res.next
        return res_l.next
        """
        解法二
        """

        if l1 and l2:
            if l1.val > l2.val:
                l1,l2 = l2,l1
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1 or l2