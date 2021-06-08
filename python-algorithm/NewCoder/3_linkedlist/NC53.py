

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        tmp = slow.next
        slow.next = slow.next.next
        tmp.next = None
        return dummy.next