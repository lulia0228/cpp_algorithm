# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        back_half_head = self.invert(slow.next)
        slow.next = None  # 打断链表

        l1, l2 = head, back_half_head
        while l2:
            tmp1 = l1.next
            l1.next = l2
            tmp2 = l2.next
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2

    def invert(self, head):
        pre = cur = head
        back = None
        while pre:
            pre = cur.next
            cur.next = back
            back = cur
            cur = pre
        return back
