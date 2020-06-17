//
// Created by LiHeng on 2020/6/15.
//

//最小硬币找零数 这道题采用了dp解法，速度不咋的；还一种方法参考L39 组合总数，转化成组合，找最小元素数目组合

#include <iostream>
#include <vector>

using namespace std ;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, -1);
        dp[0] = 0;
        for(int i=1; i<=amount; ++i){
            for(int c:coins){
                if(i >= c && dp[i-c] != -1) //一开始把i写成amount了报错
                    dp[i] = (dp[i] == -1? 1+dp[i-c]: min(dp[i], 1+dp[i-c]));
            }
        }
        return dp[amount];
    }
};

class Solution1 {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, amount+1);
        dp[0] = 0;
        for (int i=1; i<=amount; ++i) {
            for (auto coin : coins)
                if (coin <= i) //是coin<i 不是amount，容易出错
                    dp[i] = min(dp[i], dp[i-coin]+1);
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};