# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param l1 ListNode类
# @param l2 ListNode类
# @return ListNode类
#

class Solution:
    def mergeTwoLists(self, l1, l2):
        # write code here
        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode((l2.val))
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next
