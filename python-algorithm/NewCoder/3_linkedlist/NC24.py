
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 删除的是所有重复的节点（NC24），而不是保留重复的元素中的1个(NC25）

# 三指针

class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur, fut = dummy, head, head
        while fut:
            # 第一次写的时候漏掉了while fut 条件
            while fut and fut.val == cur.val:
                fut = fut.next
            if cur.next == fut:
                pre = cur
                cur = fut
            else:
                pre.next = fut
                cur = fut
        return dummy.next