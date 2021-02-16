# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        carry = 0
        while stk1 or stk2:
            sum_ = 0
            if stk1:
                sum_ += stk1.pop(-1)
            if stk2:
                sum_ += stk2.pop(-1)
            sum_ += carry
            new_node = ListNode(sum_ % 10)
            new_node.next = dummy.next
            dummy.next = new_node
            carry = sum_ // 10
        if carry:
            new_node = ListNode(1)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next




