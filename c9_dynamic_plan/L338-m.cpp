//
// Created by LiHeng on 2020/5/20.
//

//位运算+动态规划
//转移方程：状态转移函数
//P(x) = P(x/2) + (x mod 2)
//思想：一个整数和一个整数的一半（向下取余）的二进制表示只有最后一位不同，而最后一位就是奇数偶数的判定

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