
#include <iostream>
using  namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        int rev = 0 , r = x ;
        while (r != 0){
            if (rev > INT_MAX/10 || (rev == INT_MAX/10 && rev%10 > 7 ))
                return false;
            rev = rev*10 + r%10;
            r /= 10;
        }
        return rev == x ? true:false ;
    }
};

//还有一种方法是转化成字符串，从两端往中间比较，或者反转字符串比较。python操作字符串可能更方便一些