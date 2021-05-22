#--coding:utf-8--

# 前序遍历+中序遍历可以重建二叉搜索树
# 后续遍历+中序遍历可以重建二叉搜索树

# 二选一
# 因为二叉搜索树的中序遍历是有序的，因此只需要知道前序遍历或者后序遍历，排序后就可以重建二叉搜索树

# 即编码为前序遍历或后续遍历字符串；然后再重建二叉搜索树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def preorder(root):
            if root == None:
                return
            pre_ls.append(root.val)
            preorder(root.left)
            preorder(root.right)

        pre_ls = []
        preorder(root)
        return '#'.join(map(str, pre_ls))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def my_build(pre, ino, p_lt, p_rt, i_lt, i_rt):
            if p_lt > p_rt:
                return None
            root_pre = p_lt
            root_ino = record[pre[root_pre]]
            root = TreeNode(pre[root_pre])
            n_left = root_ino - i_lt
            root.left = my_build(pre, ino, p_lt + 1, p_lt + n_left, i_lt, root_ino - 1)
            root.right = my_build(pre, ino, p_lt + n_left + 1, p_rt, root_ino + 1, i_rt)
            return root

        if data == "": return None
        preorder = [int(x) for x in data.split('#')]
        inorder = sorted(preorder)
        record = {}
        for i in range(len(inorder)):
            record[inorder[i]] = i

        return my_build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans