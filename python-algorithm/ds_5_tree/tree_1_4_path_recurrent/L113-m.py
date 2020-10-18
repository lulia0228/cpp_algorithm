#--coding:utf-8--


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.find_path(root, sum, res, [])
        return res

    def find_path(self, root, sum, res, tmp):
        if root == None:
            return
        tmp.append(root.val)
        if root.left == None and root.right == None and root.val == sum:
            res.append(tmp[:])
        self.find_path(root.left, sum - root.val, res, tmp)
        self.find_path(root.right, sum - root.val, res, tmp)
        tmp.pop(-1)


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if root == None:
            return res
        self.find_path(root, sum, res, [])
        return res

    def find_path(self, root, sum, res, tmp):
        tmp.append(root.val)
        if root.left == None and root.right == None and root.val == sum:
            res.append(tmp[:])
        if root.left:
            self.find_path(root.left, sum - root.val, res, tmp)
        if root.right:
            self.find_path(root.right, sum - root.val, res, tmp)
        tmp.pop(-1)

