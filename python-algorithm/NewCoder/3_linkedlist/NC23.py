# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param x int整型
# @return ListNode类
#

# 双指针

class Solution:
    def partition(self, head, x):
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        back, cur = dummy, head
        # 先找到第一个≥x的节点
        while cur and cur.val < x:
            back = cur
            cur = cur.next
        if cur:
            # 从第一个≥x的节点cur后面找到每个＜x的点插入到cur之前
            new_back, new_cur = back, cur
            while new_cur:
                while new_cur and new_cur.val >= x:
                    new_back = new_cur
                    new_cur = new_cur.next
                if new_cur:
                    new_back.next = new_cur.next
                    back.next = new_cur
                    new_cur.next = cur
                    back = back.next
                    new_cur = new_cur.next
        return dummy.next
