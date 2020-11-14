# -*- coding: utf-8 -*-

# 6 从尾到头打印链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        if head == None:
            return res
        self.digui(head, res)
        return res

    def digui(self, head, res):
        if not head:
            return
        self.digui(head.next, res)
        res.append(head.val)