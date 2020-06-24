//
// Created by LiHeng on 2020/6/21.
//

//dp似乎有点慢，还有贪心算法做的
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std ;
class Solution {
public:
    static bool compare(vector<int> a, vector<int> b){
        return a[0] < b[0];
    }

    int findLongestChain(vector<vector<int>>& pairs) {
        int sz = pairs.size();
        //sort(pairs.begin(), pairs.end(), compare);
        sort(pairs.begin(), pairs.end(), compare);
        //dp[i]表示以pairs[i]作为结尾的最大长度
        vector<int> dp(sz,1);
        int max_len = 1;
        for(int i=1; i<sz; ++i){
            for(int j=0; j<i; ++j){
                if(pairs[i][0] > pairs[j][1]){
                    dp[i] = max(dp[i], dp[j]+1);
                    max_len = max(max_len, dp[i]);
                }
            }
        }
        return max_len;
    }

};