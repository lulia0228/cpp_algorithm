#--coding:utf-8--

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            if not p1:
                p1 = pHead2
            else:
                p1 = p1.next
            if not p2:
                p2 = pHead1
            else:
                p2 = p2.next
        return p1