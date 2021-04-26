#--coding:utf-8--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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