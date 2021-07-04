#--coding:utf-8--

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tmp = dummy
        carry = 0
        while l1 or l2:
            t_sum = 0
            if l1:
                t_sum += l1.val
                l1 = l1.next
            if l2:
                t_sum += l2.val
                l2 = l2.next
            t_sum += carry
            cur_nd = ListNode(t_sum%10)
            carry = t_sum//10
            tmp.next = cur_nd
            tmp = tmp.next
        if carry:
            cur_nd = ListNode(carry)
            tmp.next = cur_nd
            tmp = tmp.next
        return dummy.next

