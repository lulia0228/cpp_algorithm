#--coding:utf-8--

# 206 反转链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        back = None
        front = head
        while head :
            front = head.next
            head.next = back
            back = head
            head = front
        return back