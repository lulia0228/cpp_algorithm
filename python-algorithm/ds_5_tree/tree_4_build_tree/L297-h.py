# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root: return ""
        q = collections.deque()
        q.append(root)
        while q:
            cur_nd = q.popleft()
            if cur_nd:
                res.append(str(cur_nd.val))
                q.append(cur_nd.left)
                q.append(cur_nd.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        nums = data.split(",")
        root = TreeNode(int(nums[0]))
        q = collections.deque()
        q.append(root)
        cnt = 0
        while q:
            cur_nd = q.popleft()
            cnt += 1
            if nums[cnt] != "null":
                tmp_nd = TreeNode(int(nums[cnt]))
                cur_nd.left = tmp_nd
                q.append(tmp_nd)
            cnt += 1
            if nums[cnt] != "null":
                tmp_nd = TreeNode(int(nums[cnt]))
                cur_nd.right = tmp_nd
                q.append(tmp_nd)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))