

//买卖股票的最佳时机 II
//给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
//设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
//注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

//贪心算法：1 只要明天价格大于当天价格，当天就买；2 当天买第二天就卖

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for(int i = 0; i + 1 < prices.size(); ++i)
            profit += max(prices[i + 1] - prices[i], 0);
        return profit;
    }
};



