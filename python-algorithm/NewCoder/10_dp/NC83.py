#--coding:utf-8--

class Solution:
    def maxProduct(self , arr ):
        # write code here
        tmp_max = arr[0]
        tmp_min = arr[0]
        final_max = arr[0]
        for i in range(1, len(arr)):
            tmp = tmp_max
            tmp_max = max(max(tmp_max*arr[i], tmp_min*arr[i]), arr[i])
            tmp_min = min(min(tmp*arr[i], tmp_min*arr[i]), arr[i])
            final_max = max(final_max, tmp_max)
        return final_max