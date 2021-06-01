#--coding:utf-8--

# 移除重复的节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        st = set()
        pre = cur = head
        while cur:
            if cur.val in st:
                while cur and cur.val in st:
                    cur = cur.next
                pre.next = cur
            else:
                st.add(cur.val)
                pre = cur
                cur = cur.next
        return head

