

//Bit Manipulation 78 136 169 231

//思路：利用位运算及二进制性质；
//若为2的幂，则转为二进制必定有且仅有一个1，其他全为0；
#include <iostream>

using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        return (n&(n-1))==0;
    }
};



