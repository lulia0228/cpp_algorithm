#--coding:utf-8--

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        flag = head.val
        back = head
        cur = head.next
        while cur :
            if cur.val == flag:
                back.next = cur.next
            else:
                back = cur
                flag = back.val
            cur = cur.next
        return head