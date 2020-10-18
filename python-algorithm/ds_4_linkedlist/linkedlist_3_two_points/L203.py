#--coding:utf-8--


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        back = dummy
        cur = head
        while cur:
            if cur.val == val:
                back.next = cur.next
            else:
                back = cur
            cur = cur.next
        return dummy.next