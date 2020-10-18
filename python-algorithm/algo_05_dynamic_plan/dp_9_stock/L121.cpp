
//买卖股票的最佳时机
//这里提供两种方法：一种是把每天当做卖出日期，选择这一天前面的所有天中的最低价格当做卖出日期；
//另一种是动态规划，不过需要先抽象问题，转化为求价格差值序列的最大子序列和问题。

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 1)
            return 0;
        int tem_min = prices[0];
        int max_fit = 0;
        for(int i=0 ; i<prices.size() ; i++){
            tem_min = min(tem_min,prices[i]);
            max_fit = max(max_fit,prices[i]-tem_min);
        }
        return max_fit;
    }
};

class Solution1 {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 1)
            return 0;
        vector<int> subarr(prices.size()-1,0);
        for(int i=0 ;i < subarr.size();i++)
            subarr[i] = prices[i+1]-prices[i];
        //vector<int> dp(prices.size()-1);  //注释掉的是发现可以不用创建数组也可以解决
        //dp[0] = max(0,subarr[0]);
        //int final_max = dp[0];
        int last_max = max(0,subarr[0]);
        int final_max = last_max;
        for(int i=1 ;i < subarr.size() ;i++){
            //dp[i] = max(dp[i-1]+subarr[i],0);//重要
            //final_max = max(final_max,dp[i]);
            last_max = max(last_max+subarr[i],0);
            final_max = max(final_max,last_max);
        }
        return final_max;
    }
};


int main(){
    int a1[]= {7,1,5,3,6,4};
    vector<int> v1(a1,a1+5);
    cout << Solution().maxProfit(v1)<<endl;
    cout << Solution1().maxProfit(v1)<<endl;

}

