# -*- coding: utf-8 -*-


# 1 超时 收缩窗口的条件太费时间
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        lt, rt = 0, 0
        res = 1
        while rt < len(tree):
            # 开始收缩窗口
            while len(set(tree[lt:rt+1])) > 2:
                lt += 1
            res = max(res, rt-lt+1)
            rt += 1
        return res

# 2  巧妙设计下,速度快多了
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        lt, rt = 0, 0
        res = 1
        st = set()
        while rt < len(tree):
            st.add(tree[rt])
            # 开始收缩窗口
            if len(st) == 3: # 说明当前s[rt]一定是新增的种类的第一个元素
                lt = rt-2;
                while tree[lt] == tree[rt-1]:
                    lt -= 1
                st.remove(tree[lt]);
                lt += 1
            else:
                res = max(res, rt-lt+1)
            rt += 1
        return res