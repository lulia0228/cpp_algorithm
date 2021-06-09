# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head
# @return bool布尔型
#


class Solution:
    def isPail(self, head):
        # write code here
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        another_half = slow.next
        slow.next = None  # 打断

        another_half = self.reverse(another_half)
        while another_half:
            if head.val != another_half.val:
                return False
            head = head.next
            another_half = another_half.next
        return True

    def reverse(self, pHead):
        if not pHead: return None
        back = None  # 这里不需要设置虚拟头结点
        cur = pHead
        while cur:
            fut = cur.next
            cur.next = back
            back = cur
            cur = fut
        return back
