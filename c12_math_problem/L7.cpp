//
// Created by liheng on 19-9-10.
//

#include <iostream>
#include <cassert>
#include <cmath>
using namespace std ;
// 32位 [-2147483648 , 2147483647]
class Solution{
public:
    // leetcode 7 反转整数
    int reverseInt( int num ) {
        long long int result = num % 10; //必须要用long long int

        for (; num /= 10;) {   //循环中执行condition中num值顺便被改变了
            result = result * 10 + num % 10;
        }
        return (result < INT32_MIN || result > INT32_MAX)? 0:result;
    }


};


 int main(){
    int re = Solution().reverseInt(-534236469);
    cout << re << endl  ;
    bool re1 = Solution().isZhiShu(6);
    cout << re1 << endl  ;
    double re2 = Solution().mySqrt(3);
    cout << re2 << endl ;

}
