#--coding:utf-8--

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isdigit() or c.isalpha()]
        lt, rt = 0, len(new_s)-1
        while lt < rt:
            if new_s[lt] != new_s[rt]:
                return False
            lt += 1
            rt -= 1
        return True