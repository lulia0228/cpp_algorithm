# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 对比445
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        virtual = ListNode(-1)
        dummy = virtual
        carry = 0
        while l1 or l2: # 不是and
            sum_ = 0
            if l1:
                sum_ += l1.val
                l1 = l1.next # 容易忘记更新
            if l2:
                sum_ += l2.val
                l2 = l2.next # 容易忘记更新
            sum_ += carry
            dummy.next = ListNode(sum_ % 10)
            dummy = dummy.next
            carry = sum_ // 10
        if carry:
            dummy.next = ListNode(1)
        return virtual.next