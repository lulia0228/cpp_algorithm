#--coding:utf-8--

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_1, dummy_2 = ListNode(-1), ListNode(-1)
        tmp_d1, tmp_d2 = dummy_1, dummy_2
        while head:
            if head.val < x:
                tmp_d1.next = head
                tmp_d1 = tmp_d1.next
            else:
                tmp_d2.next = head
                tmp_d2 = tmp_d2.next
            head = head.next
        tmp_d2.next = None
        tmp_d1.next = dummy_2.next
        return dummy_1.next