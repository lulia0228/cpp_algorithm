#--coding:utf-8--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  类荷兰国旗 三色排序
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s = f = head
        while f:
            if f.val < x:
                s.val, f.val = f.val, s.val
                s = s.next
            f = f.next
        return head
