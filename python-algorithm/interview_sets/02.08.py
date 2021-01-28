#--coding:utf-8--

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = f = head
        while s:
            s = s.next
            if s == None: return None
            f = f.next.next
            if f == None or f.next == None: return None
            if s == f:
                break

        tmp = head
        while tmp != s:
            tmp = tmp.next
            s = s.next
        return s
