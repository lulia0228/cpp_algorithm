# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
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


# 递归写法

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        new_head = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return new_head

