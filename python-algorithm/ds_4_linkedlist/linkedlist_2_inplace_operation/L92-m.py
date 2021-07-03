#--coding:utf-8--


# back cur fut 分别表示上一个节点 当前节点 下一个节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        break_point = dummy
        cur = dummy
        cnt = 0
        while cnt < left:
            break_point = cur  # 标记反转起始位置上一个点
            cur = cur.next
            cnt += 1

        old_start = cur        # 标记反转起始位置
        back = fut = None
        while cnt <= right:
            fut = cur.next
            cur.next = back
            back = cur
            cur = fut
            cnt += 1

        break_point.next = back
        old_start.next = fut

        return dummy.next


