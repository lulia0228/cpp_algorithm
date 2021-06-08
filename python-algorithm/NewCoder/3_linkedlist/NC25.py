# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 不是删除的是所有重复的节点(NC24），而是保留重复的元素中的1个(NC25）

# 双指针

class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        if not head: return None
        cur = fut = head
        while fut:
            while fut and fut.val == cur.val:
                fut = fut.next
            cur.next = fut
            cur = cur.next
        return head