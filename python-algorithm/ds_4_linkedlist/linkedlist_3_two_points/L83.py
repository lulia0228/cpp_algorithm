#--coding:utf-8--

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        back = head
        cur = head.next
        while cur:
            if cur.val == back.val:
                cur = cur.next
            else:
                back.next = cur
                back = cur
                cur = cur.next
        # 这句容易漏掉，处理最后是多个重复的数字
        back.next = None
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        flag = head.val
        back = head
        cur = head.next
        while cur :
            if cur.val == flag:
                back.next = cur.next
                cur = cur.next
            else:
                back = cur
                flag = back.val
                cur = cur.next
        return head