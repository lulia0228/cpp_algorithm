//
// Created by LiHeng on 2020/6/21.
//

//硬币找零组合数

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount+1, 0);
        dp[0] = 1;
        for(auto c:coins){
            for(int i=1; i<=amount; ++i) //或者直接i=c开始下面不需要判断i>=c
                if(i>=c && dp[i-c] != 0)
                    dp[i] += dp[i-c];
        }
        return dp[amount];
    }
};

// 这道题做的时候，直接套用322，在内层循环币种，外层循环金额，出现的问题是子问题中出现重复组合
// 为了解决这个问题，内环层循环进行了颠倒，就避免了重复子问题
// 可以自己用conis=[1,2] amount=3 手推下