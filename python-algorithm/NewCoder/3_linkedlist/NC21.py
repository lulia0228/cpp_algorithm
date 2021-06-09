# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head, m, n):
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        cnt = 0
        break1 = dummy
        start = dummy
        while cnt < m:
            cnt += 1
            break1 = start
            start = start.next
        back, cur = None, start

        # 让cur到达第n个节点的下一个节点位置
        # 第一次写错 写成cnt < n 导致第n个位置未反转
        while cnt <= n:
            cnt += 1
            fut = cur.next
            cur.next = back
            back = cur
            cur = fut
        break1.next = back
        start.next = cur
        return dummy.next

