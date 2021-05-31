#--coding:utf-8--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None : return l2
        if l2 == None : return l1
        new_head = ListNode(-1)
        tmp_node = new_head
        carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10
            tmp_node.next = ListNode(sum%10)
            tmp_node = tmp_node.next
        if carry == 1:
            tmp_node.next = ListNode(1)
        return new_head.next
