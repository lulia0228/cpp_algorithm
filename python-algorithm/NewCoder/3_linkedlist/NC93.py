#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#

class My_node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.r_c = {}
        self.head = My_node(-1, -1)
        self.tail = My_node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head

    def LRU(self, operators, k):
        # write code here
        res = []
        for ops in operators:
            if ops[0] == 1:
                self.My_set(ops, k)
            else:
                res.append(self.My_get(ops))
        return res

    def My_set(self, ops, k):
        if ops[1] in self.r_c:  # 覆盖掉
            self.r_c[ops[1]].val = ops[2]
            # 移动到链首
            self.move2head(self.r_c[ops[1]])
        else:
            # 删除最不常用的
            if len(self.r_c) == k:
                del self.r_c[self.tail.left.key]
                self.tail.left.left.right = self.tail
                self.tail.left = self.tail.left.left
            # 插入到链首
            tmp = My_node(ops[1], ops[2])
            self.r_c[ops[1]] = tmp
            tmp.right = self.head.right
            self.head.right.left = tmp
            tmp.left = self.head
            self.head.right = tmp

    def My_get(self, ops):
        if ops[1] not in self.r_c:
            return -1
        # 移动到链首
        nd = self.r_c[ops[1]]
        self.move2head(nd)
        return nd.val

    def move2head(self, nd):
        nd.left.right = nd.right
        nd.right.left = nd.left
        nd.right = self.head.right
        self.head.right.left = nd
        nd.left = self.head
        self.head.right = nd


OPS = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
K = 3

res = Solution().LRU(OPS, K)
print(res)

