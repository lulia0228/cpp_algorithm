//
// Created by liheng on 19-9-10.
//

#include <iostream>
#include <cassert>
#include <cmath>

using namespace std ;
// 32位 [-2147483648 , 2147483647]
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x){
            res = res*10 + x%10;
            x /= 10;
        }
        if(res < INT32_MIN || res > INT32_MAX)
            return 0;
        return res;
    }

};


 int main(){
    int re = Solution().reverse(-534236469);
    cout << re << endl  ;
    return 0;

}
