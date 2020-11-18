#--coding:utf-8--

# 给定一个数组，判断是不是一个二叉搜索树的后序遍历

# 分治法，这道题有点难  可以和leetcode 105 106理解


# 1 思路：
# 根据二叉搜索树的定义，可以通过递归，判断所有子树的正确性 （即其后序遍历是否满足二叉搜索树的定义） ，
# 若所有子树都正确，则此序列为二叉搜索树的后序遍历。

# 2 递归解析：
# 终止条件：当i≥j，说明此子树节点数量≤1，无需判别正确性，因此直接返回true ；
# 递推工作
# （1）划分左右子树： 遍历后序遍历的[i,j] 区间元素，寻找第一个大于根节点的节点，索引记为m 。
#     此时，可划分出左子树区间[i,m-1]、右子树区间[m,j−1]、根节点索引j 。
# （2）判断是否为二叉搜索树：
#     a.左子树区间[i,m−1]内的所有节点都应<postorder[j]。而第1.划分左右子树步骤已经保证左子树区间的正确性，
#        因此只需要判断右子树区间即可。
#     b.右子树区间[m,j−1]内的所有节点都应>postorder[j]。实现方式为遍历，当遇到postorder[j]≤postorder[j]的
#        节点则跳出；则可通过p=j 判断是否为二叉搜索树。

# 3 返回值：
# 所有子树都需正确才可判定正确，因此使用 与逻辑符and 连接。
# (1) p=j:判断 此树 是否正确。
# (2) recur(i,m−1):判断 此树的左子树 是否正确。
# (3) recur(m,j−1):判断 此树的右子树 是否正确。



class Solution:

    def verifyPostorder(self, postorder: List[int]) -> bool:
        
        def recur(i, j):
            # 当i≥j ，说明此子树节点数量≤1，无需判别正确性，因此直接返回true
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
