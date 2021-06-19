#--coding:utf-8--
#
# max increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型
#

class Solution:
    def MLS(self , arr ):
        # write code here
        st = set(arr)
        ans = 0
        for n in arr:
            if n-1 not in st:
                cnt = 1
                nxt = n+1
                while nxt in st:
                    st.remove(nxt)
                    nxt += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans