#--coding:utf-8--

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 相当于开辟了2个新链表
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_1, dummy_2 = ListNode(-1), ListNode(-1)
        tmp_d1, tmp_d2 = dummy_1, dummy_2
        while head:
            if head.val < x:
                tmp_d1.next = head
                tmp_d1 = tmp_d1.next
            else:
                tmp_d2.next = head
                tmp_d2 = tmp_d2.next
            head = head.next
        tmp_d2.next = None
        tmp_d1.next = dummy_2.next
        return dummy_1.next

# 不开辟新链表的做法
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1, head)
        back = dummy
        cur = head
        while cur and cur.val<x:
            back = cur
            cur = cur.next
        if cur == None:
            return head
        new_back = cur
        new_cur = cur.next
        while new_cur:
            if new_cur.val<x:
                new_back.next = new_cur.next
                # 把当前节点插到前面末尾
                new_cur.next = cur
                back.next = new_cur
                back = new_cur
                new_cur = new_back.next
            else:
                new_back = new_cur
                new_cur = new_cur.next
        return dummy.next