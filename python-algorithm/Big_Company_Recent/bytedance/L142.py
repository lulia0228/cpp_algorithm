# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if flag:
            tmp = head
            while tmp != slow:
                tmp = tmp.next
                slow = slow.next
            return tmp
        return None


