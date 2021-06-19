#--coding:utf-8--

# 插入排序的思想
class Solution:
    def reOrderArray(self , array ):
        # write code here
        i, j = 0, 0
        while j < len(array):
            if array[j]&1 :
                tmp = array[j]
                for k in range(j, i, -1): # 不倒序会覆盖
                    array[k] = array[k-1]
                array[i] = tmp
                i += 1
                j += 1
            else:
                j += 1
        return array


arr = [34,1,3,5,23,12,67,101,8,42,34,56]
res = Solution().reOrderArray(arr)
print(res)