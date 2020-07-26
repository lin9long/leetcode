# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    19. 删除链表的倒数第N个节点
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        count = 1
        dic = {}
        while head:
            # node = head.val
            dic[count] = ListNode(head.val)
            count += 1
            head = head.next
        # print(dic,count-1,n)
        count = count - 1
        start = count - n
        end = count - n + 2

        ret = ListNode(None)
        tmp = ret
        s = 1
        while s <= start:
            tmp.next = dic[s]
            tmp = tmp.next
            s += 1
        s = end
        while s <= count and s >= end:
            tmp.next = dic[s]
            tmp = tmp.next
            s += 1

        return ret.next