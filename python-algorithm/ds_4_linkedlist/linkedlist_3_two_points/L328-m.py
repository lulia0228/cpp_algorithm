#--coding:utf-8--
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = odd.next
        ano_half = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        # 连接2个段
        odd.next = ano_half
        return head