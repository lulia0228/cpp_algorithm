# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#


class Solution:
    def addInList(self, head1, head2):
        # write code here
        stk1 = []
        stk2 = []
        while head1:
            stk1.append(head1.val)
            head1 = head1.next
        while head2:
            stk2.append(head2.val)
            head2 = head2.next
        carry = 0
        dummy = ListNode(-1)
        while stk1 or stk2:
            sum_ = 0
            if stk1:
                sum_ += stk1.pop()
            if stk2:
                sum_ += stk2.pop()
            sum_ += carry
            cur_nd = ListNode(sum_ % 10)
            cur_nd.next = dummy.next
            dummy.next = cur_nd
            carry = sum_ // 10
        if carry > 0:
            cur_nd = ListNode(carry)
            cur_nd.next = dummy.next
            dummy.next = cur_nd
        return dummy.next






