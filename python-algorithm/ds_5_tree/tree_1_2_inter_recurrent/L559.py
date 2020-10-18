#--coding:utf-8--

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        tmp_depth = [0]*len(root.children)
        for i in range(len(root.children)):
            tmp_depth[i] = self.maxDepth(root.children[i])
        return max(tmp_depth)+1 if tmp_depth!=[] else 1