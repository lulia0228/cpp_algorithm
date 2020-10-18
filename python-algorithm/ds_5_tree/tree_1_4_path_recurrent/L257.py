#--coding:utf-8--


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.find_path(root, res, [])
        res = ["->".join(item) for item in res]
        return res

    def find_path(self, root, res, tmp):
        if root == None:
            return
        tmp.append(str(root.val))
        if root.left == None and root.right == None:
            res.append(tmp[:])
        self.find_path(root.left, res, tmp)
        self.find_path(root.right, res, tmp)
        tmp.pop(-1)