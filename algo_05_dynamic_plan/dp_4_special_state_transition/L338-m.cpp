

//位运算+动态规划
//转移方程：状态转移函数
//P(x) = P(x/2) + (x mod 2)
//思想：一个整数和一个整数的一半（向下取余）的二进制表示只有最后一位不同，而最后一位是奇数偶数的判定

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num+1, 0);
        for(int i=1; i<=num; ++i)
            res[i] = res[i>>1] + (i&1);
        return res;
    }
};

//另外一个思路，也是动态规划 转移状态方程：dp[i] = dp[i&(i-1)] + 1;