#--coding:utf-8--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 自己写的
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-101)
        dummy.next = head
        back = dummy
        cur = head
        while cur:
            fut = cur.next
            while fut and fut.val==cur.val:
                fut = fut.next
            # 处理多个相同值结尾的情况
            if fut == None:
                back.next = None
            if cur.next == fut:
                back.next = cur
                back = cur
                cur = fut
            else:
                cur = fut
        return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.next.val == cur.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next # 永远指向不重复的下一个位置
            else:
                cur = cur.next

        return dummy.next