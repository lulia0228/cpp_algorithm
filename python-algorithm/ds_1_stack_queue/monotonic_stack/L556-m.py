#--coding:utf-8--


# 下一个更大的元素III

# 倒序遍历，找到当前值右侧大于它的值中最小的那个，与其交换；然后当前值右侧所有值从小到大排序
# 利用单调栈找到当前值右侧大于它的最小值的索引
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        INF = pow(2,31)-1 # 2147483647
        n, stack = list(str(n)), []
        for i in range(len(n)-1, -1, -1):
            j = -1
            while stack and n[stack[-1]]>n[i]: #单调递增栈
                j=stack.pop() #找到栈内最小的大于当前元素的值
            if j>=0:
                n[i], n[j] = n[j], n[i]  #调换找到的值
                # n = n[:i+1]+sorted(n[i+1:]) #后面的值重排
                n = n[:i+1]+n[i+1:][::-1] #后面的值倒序就可以了
                n = int(''.join(n))
                return n if n<=INF else -1
            stack.append(i)
        return -1