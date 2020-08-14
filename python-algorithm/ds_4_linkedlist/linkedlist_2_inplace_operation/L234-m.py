#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        # 循环结束 当链表长度为奇数，slow指向正中间；偶数，slow指向前半段的最后位置
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        back = None
        cur = slow.next
        while cur:
            front = cur.next
            cur.next = back
            back = cur
            cur = front
        slow.next = back
        # back 成了后半段的起始点
        while back:
            if back.val != head.val:
                return False
            back = back.next
            head = head.next
        return True