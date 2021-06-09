# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head node
# @return ListNode类
#

class Solution:
    def sortInList(self, head):
        # write code here
        # 返回条件 不能少了not head.next
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        ano_half = slow.next
        slow.next = None
        l1 = self.sortInList(head)
        l2 = self.sortInList(ano_half)
        return self.merge2List(l1, l2)

    def merge2List(self, l1, l2):
        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode((l2.val))
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next

