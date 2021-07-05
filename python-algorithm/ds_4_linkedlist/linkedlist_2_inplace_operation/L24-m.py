#--coding:utf-8--

# 这道题是三个指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        back = dummy
        cur = head
        # 三指针
        while cur and cur.next:
            fut = cur.next
            cur.next = fut.next
            fut.next = cur
            back.next = fut
            back = cur
            cur = cur.next
        return dummy.next