

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return bool布尔型
#

class Solution:
    def hasCycle(self , head ):
        # write code here
        if not head : return False

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


