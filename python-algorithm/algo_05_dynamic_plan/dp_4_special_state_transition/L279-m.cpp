

//使用的DP,另外一种方法是图遍历

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = 0;
        for(int i=1; i<=n; ++i){
            int s = 1;
            int min_num = i; //i个1  最开始这个代码放错位置了，必须放在循环里面
            while(i-s*s >= 0){
                min_num = min(min_num, dp[i-s*s] + 1); //注意啊 是i-s*s 不是n-s*s ，当前遍历求得是到整数i的平方数路径最短
                s++;
            }
            dp[i] = min_num;
        }
        return dp[n];
    }
};