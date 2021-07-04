# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 反转后半段链表
        ano_half = self.reverse(slow.next)
        while ano_half:
            if head.val != ano_half.val:
                return False
            head = head.next
            ano_half = ano_half.next
        return True

    def reverse(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
