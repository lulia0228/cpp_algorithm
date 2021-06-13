import collections
class Solution:
    def solve(self, xianxu, zhongxu):
        # write code here
        sz = len(xianxu)
        idx_in = {}
        for idx, n in enumerate(zhongxu):
            idx_in[n] = idx
        res = self.rebuild_(xianxu, zhongxu, 0, sz - 1, 0, sz - 1, idx_in)

        return self.rightSideView(res)

    def rebuild_(self, xianxu, zhongxu, p_st, p_ed, i_st, i_ed, idx_zhongxu):
        if p_ed < p_st:
            return None
        r_val = xianxu[p_st]
        r_in_zhongxu = idx_zhongxu[r_val] # 当前根节点在中序中的下标
        root = TreeNode(r_val)
        nums_of_left = r_in_zhongxu - i_st
        root.left = self.rebuild_(xianxu, zhongxu, p_st + 1, p_st + nums_of_left, i_st, r_in_zhongxu - 1, idx_zhongxu)
        root.right = self.rebuild_(xianxu, zhongxu, p_st + nums_of_left + 1, p_ed, r_in_zhongxu + 1, i_ed, idx_zhongxu)
        return root

    # 右视图除了用层序遍历BFS，也可以用DFS方法做
    def rightSideView(self, root):
        res = []
        if root == None: return res
        que = collections.deque()
        que.append(root)
        while que:
            sz = len(que)
            for i in range(sz):
                cur_node = que.popleft()
                if i == sz - 1:
                    res.append(cur_node.val)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
        return res