#--coding:utf-8--
'''
@Time   : 2020/8/13
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        carry = False
        while l1 != None or l2 != None:
            tmp_sum = 0
            if l1 != None:
                tmp_sum += l1.val
                l1 = l1.next
            if l2 != None:
                tmp_sum += l2.val
                l2 = l2.next
            if carry:
                tmp_sum += 1
            cur.next = ListNode(tmp_sum%10)
            cur = cur.next
            carry = True if tmp_sum>=10 else False
        if carry:
            cur.next = ListNode(1)
        return dummy.next