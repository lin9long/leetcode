#!/usr/bin/python
# -*-coding:utf-8 -*-

"""
-------------------------------------------------
   File Name：     main.py
   Description :   
   Author :        linlongzhen
   date：          2019/4/1
-------------------------------------------------
   Change Activity:
                   2019/4/1
-------------------------------------------------
"""
import sys
import os
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
    def __str__(self):
        return """val {},next {}""".format(self.val,self.next)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        v_1 = head.val
        node_list = []
        while head.next :
            node_list.append(head)
            head = head.next
            if head is None:
                break
            v_2 = head.val
            print(v_1,v_2)
            if v_1 == v_2:
                v_1 = v_2
                node_list.pop()
            else:
                node_list.append(head)
        for i in node_list:
            print(i)

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l4.next = None
    l1.next = l2
    l2.next = l3
    l4.next = l4
    s.deleteDuplicates(l1)