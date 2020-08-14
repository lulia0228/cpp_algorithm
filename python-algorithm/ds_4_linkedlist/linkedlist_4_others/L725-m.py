#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = [None for i in range(k)]
        if not root:
            return res
        tail = root
        lenth = 1
        while tail.next:
            tail = tail.next
            lenth += 1
        base = lenth//k
        addtion = lenth%k
        cur = root
        for i in range(k):
            if cur:
                res[i] = cur
                curSize = base + (1 if addtion >= 1 else 0)
                for j in range(curSize-1):
                    cur = cur.next
                new_start = cur.next
                cur.next = None # 断开
                cur = new_start
                addtion -= 1
        return res