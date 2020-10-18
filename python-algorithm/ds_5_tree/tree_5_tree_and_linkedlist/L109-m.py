# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 和108题思路一致，只是这里输入变成链表

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        pre, slow, fast = None, head, head
        # 找到链表中间节点
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        new_start = slow.next
        # 中间节点作为根节点
        root = TreeNode(slow.val)
        # pre = NULL说明中间节点恰好就是链表头节点,特殊处理
        root.left = None if pre==None else self.sortedListToBST(head)
        root.right = self.sortedListToBST(new_start)
        return root