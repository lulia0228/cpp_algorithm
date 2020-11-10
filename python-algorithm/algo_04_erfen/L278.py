#--coding:utf-8--

# 第一个错误的版本

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lt, rt = 1, n
        while lt < rt:
            mid  = lt + (rt-lt)//2
            if isBadVersion(mid):
                rt  = mid
            else:
                lt = mid + 1
        return lt


class Solution1:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lt, rt = 1, n
        while lt <= rt:
            mid  = lt + (rt-lt)//2
            if isBadVersion(mid):
                rt = mid - 1
            else:
                lt = mid + 1
        return lt