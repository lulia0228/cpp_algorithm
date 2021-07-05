#--coding:utf-8--

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stk = []
        cursor = root
        cnt = 0
        # 逆中序遍历
        while stk or cursor:
            while cursor:
                stk.append(cursor)
                cursor = cursor.right
            cursor = stk.pop()
            cnt += 1
            if cnt == k: return cursor.val
            cursor = cursor.left