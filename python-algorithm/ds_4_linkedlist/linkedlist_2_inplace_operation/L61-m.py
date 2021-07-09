#--coding:utf-8--

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        cnt = 1
        tail = head
        # 计算出链表长度并标记最后个节点
        while tail.next:
            cnt += 1
            tail = tail.next
        if k%cnt == 0:
            return head
        slow = fast = head
        for _ in range(k%cnt):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        tail.next = head
        return new_head
