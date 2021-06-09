# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return void
#


class Solution:
    def reorderList(self, head):
        # write code here
        if not head: return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        ano_half = slow.next
        slow.next = None
        ano_half = self.reverse(ano_half)
        p1 = head
        p2 = ano_half
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        return head

    def reverse(self, pHead):
        # write code here
        if not pHead: return None
        back = None  # 这里不需要设置虚拟头结点
        cur = pHead
        while cur:
            fut = cur.next
            cur.next = back
            back = cur
            cur = fut
        return back