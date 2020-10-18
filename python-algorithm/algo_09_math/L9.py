# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        rev = 0
        tmp = x
        while tmp :
            rev = rev*10 + tmp%10
            tmp = tmp//10
        return rev == x