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

    //求一个数的平方根 L69
    double mySqrt(int x) {
        if(x == 0 ) return 0;
        double precision = 1.0e-7, start = 0, end = x;
        if(x < 1)
            end = 1;
        while(end - start > precision)
        {
            double mid = start + (end-start) / 2;
            if( mid == x / mid) return mid;
            else if(mid > x/mid) end = mid;
            else start = mid;
        }
        return start + (end - start)/2;
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
