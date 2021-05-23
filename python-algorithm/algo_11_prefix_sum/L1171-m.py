# -*- coding: utf-8 -*-

# 前缀和+哈希

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        presum_lastNode_dic = defaultdict(ListNode)

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        cur_presum = 0
        while p:
            cur_presum += p.val
            presum_lastNode_dic[cur_presum] = p  # 取前缀和的最右的一个结点
            p = p.next

        cur_presum = 0
        p = dummy
        while p:
            cur_presum += p.val
            p.next = presum_lastNode_dic[cur_presum].next  # 2个结点中间，都直接删除了 要么就只有自己1个结点
            p = p.next

        return dummy.next
