#--coding:utf-8--

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root: return res
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, target, tmp, res):
        if not root.left and not root.right:
            if target == root.val:
                tmp.append(root.val)
                res.append(tmp[:])
                tmp.pop()
            return
        tmp.append(root.val)
        if root.left:
            self.dfs(root.left, target-root.val, tmp, res)
        if root.right:
            self.dfs(root.right, target-root.val, tmp, res)
        tmp.pop()


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root: return res
        self.dfs(root, 0, targetSum, [], res)
        return res

    def dfs(self, root, cur_sum, target, tmp, res):
        if not root: return
        if not root.left and not root.right and cur_sum == target-root.val:
            tmp.append(root.val)
            res.append(tmp[:])
            tmp.pop()
            return
        tmp.append(root.val)
        self.dfs(root.left, cur_sum+root.val, target, tmp, res)
        self.dfs(root.right,cur_sum+root.val, target, tmp, res)
        tmp.pop()

