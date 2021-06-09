# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#

class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        dummy = ListNode(-1)
        dummy.next = pHead
        slow = dummy
        fast = dummy
        cnt = 0
        while cnt < k and fast.next:
            cnt += 1
            fast = fast.next
        if cnt < k:
            return None
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
