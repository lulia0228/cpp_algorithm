#--coding:utf-8--


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        tail = head # 标记尾节点
        lenth = 1
        while tail.next:
            lenth += 1
            tail = tail.next
        if k%lenth == 0:
            return head
        last = head # 断开位置上一个节点
        for i in range(lenth-k%lenth-1):
            last = last.next
        new_head = last.next
        tail.next = head
        last.next = None
        return new_head