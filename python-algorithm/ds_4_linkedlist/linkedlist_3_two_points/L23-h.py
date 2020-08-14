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

# 使用数组模拟队列，两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return None
        que = []
        for lk in lists:
            que.append(lk)
        while len(que) > 1:
            l1 = que.pop(0)
            l2 = que.pop(0)
            tmp = self.merge2Lists(l1, l2)
            que.append(tmp)
        return que[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2 :
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next