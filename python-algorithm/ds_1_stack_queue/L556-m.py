#--coding:utf-8--

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        INF = pow(2,31)-1 # 2147483647
        n, stack = list(str(n)), []
        for i in range(len(n)-1, -1, -1):
            j = -1
            while stack and n[stack[-1]]>n[i]: #单调递增栈
                j=stack.pop() #找到栈内最小的大于当前元素的值
            if j>=0:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp      #调换找到的值
                n = n[:i+1]+sorted(n[i+1:]) #后面的值重排
                n = int(''.join(n))
                print(n)
                return n if n<=INF else -1
            stack.append(i)
        return -1

print(Solution().nextGreaterElement(2147483486))
                                  # 2147483648

