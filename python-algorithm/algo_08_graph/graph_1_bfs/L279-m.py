#--coding:utf-8--


# 模拟树的层序遍历

class Solution:
    def numSquares(self, n: int) -> int:
        que = []
        que.append(n)
        flag = [False for i in range(n+1)]
        level = 0
        while que != []:
            cur_level_size = len(que)
            level += 1
            for idx in range(cur_level_size):
                tmp = que.pop(0)
                s = 1
                while tmp-s*s >= 0:
                    val = tmp-s*s
                    if  val == 0:
                        return level
                    if not flag[val]:
                        que.append(val)
                        flag[val] = True
                    s += 1
        return 0


# 相同思路，另一种写法
class Solution1:
    def numSquares(self, n: int) -> int:
        que = []
        que.append((0,0))
        flag = [False for i in range(n+1)]
        while que != []:
            cur_node = que.pop(0)
            tmp = cur_node[0]
            step = cur_node[1]
            s = 1
            while tmp + s*s <= n:
                val = tmp + s*s
                if val == n:
                    return step+1
                if not flag[val]:
                    que.append((val, step+1))
                    flag[val] = True
                s += 1
        return 0