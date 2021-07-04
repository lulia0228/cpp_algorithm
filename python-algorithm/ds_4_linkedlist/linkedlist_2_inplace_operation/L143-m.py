#--coding:utf-8--
# 重排链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        ano_half = self.reverse(slow.next)
        slow.next = None # 断开原链表

        # 题目要求返回None；所以就不要开辟新的头节点了
        l1, l2 = head, ano_half
        while l2:
            tmp_1 = l1.next
            l1.next = l2
            tmp_2 = l2.next
            l2.next = tmp_1

            l1 = tmp_1
            l2 = tmp_2

    def reverse(self, head):
        if not head or not head.next: return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head





