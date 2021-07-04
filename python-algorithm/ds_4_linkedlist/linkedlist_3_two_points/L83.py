#--coding:utf-8--
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                # x = cur.val
                # while cur.next and cur.next.val == x:
                #     cur.next = cur.next.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# 自己写的
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


