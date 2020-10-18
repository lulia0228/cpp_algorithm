# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 15:56
# @Author  : No Name

# 优化了空间复杂度，在遍历的过程中确定，不是将全部元素记录到数组中，再处理数组
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        pre = 0
        idx, cnt, max_freq = 0, 0, 0
        stk = []  # 模拟栈
        while stk != [] or root != None:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop(-1)
            idx += 1

            if idx == 1:
                pre = root.val
                cnt = 1
                max_freq = 1
            else:
                if root.val != pre:
                    if cnt > max_freq:
                        res = [pre]
                    elif cnt == max_freq:
                        res.append(pre)
                    max_freq = max(max_freq, cnt)
                    pre = root.val
                    cnt = 1
                else:
                    cnt += 1
            root = root.right

        # 最后的元素未作比较
        if cnt > max_freq:
            return [pre]
        elif cnt == max_freq:
            res.append(pre)
        return res