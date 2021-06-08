# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import collections
class Solution:
    def mergeKLists(self , lists):
        # write code here
        if not lists: return None
        que = collections.deque(lists)
        while len(que)>1:
            l1 = que.popleft()
            l2 = que.popleft()
            que.append(self.merge2List(l1, l2))
        return que.popleft()

    def merge2List(self, l1, l2):
        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        if l1: tmp.next = l1
        else: tmp.next = l2
        return dummy.next


# 优先级队列（好像更快一些）
class Solution:
    def mergeKLists(self , lists ):
        # write code here
        import heapq
        dump= ListNode(0)
        p = dump
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dump.next

# 优先级队列的构建时间是线性O(n) 并不是nlogn。
# 因为不是每一层向下调整的次数都是树的最大高度，所以累加之后发现是线性时间复杂度