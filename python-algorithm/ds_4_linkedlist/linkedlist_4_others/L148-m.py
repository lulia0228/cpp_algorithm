#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = fast = head
        bre = head  # 记录打断位置上一个节点
        while fast and fast.next:
            bre = slow
            slow = slow.next
            fast = fast.next
        bre.next = None
        lt = self.sortList(head)
        rt = self.sortList(slow)
        return self.merge2Lists(lt, rt)

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next

    