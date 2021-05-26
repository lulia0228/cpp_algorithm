#--coding:utf-8--

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# （1）满二叉树，level从上到下计数且从0开始计数
# （2）节点排序从1计数，则最后一层节点起始为pow(2,level),最后一层节点个数不定，
#     最后一个节点的排序号为【pow(2,level), pow(2,level+1)-1】闭区间
# （3）每个节点排序号的二进制编码除了最高位置的1，剩下的可以从根节点遍历到当前节点
#     （左节点为0，右节点为1表示，如此可快速定位节点）
# （4）在最后一个节点的排序号所属范围内进行二分查找，确定最后一个节点

# 时间复杂度O(level^2)  level~logN

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        level = 0
        tmp = root
        while tmp.left:
            level += 1
            tmp = tmp.left

        lt, rt = pow(2,level), pow(2, level+1)-1
        while lt < rt:
            mid = lt + (rt-lt+1)//2 # 为什么有时候要+1？没搞清楚
            if self.exist(root, level, mid):
                lt = mid
            else:
                rt = mid - 1
        return lt

    def exist(self, root, level, k):
        bits = 1 << (level-1)
        nd = root
        while nd and bits:
            if bits & k :
                nd = nd.right
            else:
                nd = nd.left
            bits >>= 1
        return True if nd else False