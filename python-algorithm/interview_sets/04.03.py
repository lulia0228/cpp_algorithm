#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree: return []
        res = []
        que = []
        que.append(tree)
        while que:
            sz = len(que)
            new_head = ListNode(-1)
            tmp_lk = new_head
            for i in range(sz):
                node = que.pop(0)
                tmp_lk.next = ListNode(node.val)
                tmp_lk = tmp_lk.next
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(new_head.next)
        return res
