#--coding:utf-8--
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param a string字符串 待计算字符串
# @return int整型
#
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param a string字符串 待计算字符串
# @return int整型
#


# 和lc 1044 不一样


class Solution:
    def solve(self , a ):
        # write code here
        n=len(a)
        if n<2:
            return 0
        for window in range(n//2,-1,-1):
            count=0
            for j in range(n-window):
                if a[j]==a[j+window]:
                    count+=1
                else:
                    count=0
                    # 剪枝操作
                    if n - window < 2 * j:
                        break
                if count==window:
                    return 2*window
        return 0