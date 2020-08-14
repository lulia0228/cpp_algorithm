#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''


# 这道题依然是三个指针，只是每次往后移动2步

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        back = dummy
        cur = head
        while cur and cur.next:
            front = cur.next
            back.next = front
            cur.next = front.next
            front.next = cur
            back = cur
            cur = back.next
        return dummy.next
