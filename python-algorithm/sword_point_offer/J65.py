#--coding:utf-8--

# 不用加减乘除做加法
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

'''
Python 负数的存储：
Python，Java 等语言中的数字都是以 补码 形式存储的。
但 Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
（1）获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。
可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为0），
从无限长度变为一个 32 位整数。
（2）返回前数字还原： 若补码 a 为负数（ 0x7fffffff 是最大的正数的补码 ），
需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 1 至 32 位按位取反；
~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
'''

print(0xffffffff)
print(-1&0xffffffff)
print(pow(2,32)-1)

