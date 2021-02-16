# -*- coding: utf-8 -*-
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if  len(lists) == 0: return None
        que = lists
        while len(que) != 1:
            f1 = que.pop(0)
            f2 = que.pop(0)
            que.append(self.merge2Lists(f1, f2))
        return que.pop(0)

    def merge2Lists(self, l1, l2):
        virtual_head = ListNode(-1)
        dummy = virtual_head
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return virtual_head.next