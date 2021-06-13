# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param head TreeNode类
# @return int整型
#
class Solution:
    def nodeNum(self, head):
        # write code here
        if not head: return 0
        level = 0
        tmp = head
        while tmp.left:
            level += 1
            tmp = tmp.left
        if level == 0: return 1
        lt, rt = pow(2, level), pow(2, level + 1) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if not self.exist(head, level, mid):
                rt = mid - 1
            else:
                lt = mid + 1
        return lt - 1

    # 对完全二叉树每个节点做霍夫曼编码，左0，右1 根节点除外 根节点1(对应的值刚好是节点的序号)
    # 例如序号12  完全二叉树树中编码 1100 ；只需对根节点除外进行每个二进制位上的左右判断，搜索节点
    def exist(self, root, level, mid):
        slide = 1 << (level - 1)
        nd = root
        while nd and slide:
            if slide & mid:
                nd = nd.right
            else:
                nd = nd.left
            slide >>= 1
        return True if nd else False


