#--coding:utf-8--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # nextHead指向链表中除去k个节点之后的头节点
        # 初始指向节点head
        nextHead = head
        # // 链表中剩余节点个数
        remainNum = 0;
        while remainNum < k:
            # 根据题意如果链表剩余节点个数不足k个
            # 则不需要反转，因此直接返回head
            if nextHead == None:
                return head
            remainNum += 1
            nextHead = nextHead.next

        # 递归反转链表中除去前k个节点的后续节点,返回
        subList = self.reverseKGroup(nextHead, k)
        # 未除去前K个节点前翻转前k个后得到的新的头节点
        newHead = self.reverseTopN(head, k)
        # 前k个节点反转后，head指向的节点是反转后的链表中的最后一个节点
        # 因此head指向的节点的后继指针指向subList
        head.next = subList

        return newHead

    def reverseTopN(self, head, n):
        pre = None
        cur, fur = head, head
        cnt = 0
        while cnt < n:
            fur = cur.next
            cur.next = pre
            pre = cur
            cur = fur
            cnt += 1
        return pre




