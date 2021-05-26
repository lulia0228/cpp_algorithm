#--coding:utf-8--


class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        num：当前区间整数个数，如9,90,900……
        cnt：当前区间正整数包含数字的个数，如整数123，则cnt=3
        target：目标正整数，即查找的第n位数字在正整数target中
        index：查找结果在整数target中的第几位
        '''
        num = 9
        cnt = 1
        #计算n在哪个区间
        while n > num*cnt:
            n -= num*cnt
            cnt += 1
            num *= 10
        #计算目标数
        target = num//9 + (n-1)//cnt
        #计算在目标数的第几位
        index=(n-1)%cnt
        return int(str(target)[index])
