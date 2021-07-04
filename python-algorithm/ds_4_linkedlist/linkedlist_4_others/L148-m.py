#--coding:utf-8--
# 排序链表（归并）
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # not head.next 不能没有
        if not head or not head.next: return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        ano_half = slow.next
        slow.next = None
        lt = self.sortList(head)
        rt = self.sortList(ano_half)
        return self.merge(lt, rt)

    def merge(self, h1, h2):
        if not h1: return h2
        if not h2: return h1
        dummy = ListNode(0)
        cursor = dummy  # 重新开辟一个指针，方便后面返回dummy.next
        while h1 and h2:
            if h1.val <= h2.val:
                cursor.next = h1
                h1 = h1.next
            else:
                cursor.next = h2
                h2 = h2.next
            cursor = cursor.next
        # 太容易漏掉了
        if h1:
            cursor.next = h1
        if h2:
            cursor.next = h2

        return dummy.next
    