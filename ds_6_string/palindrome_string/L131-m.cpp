//
// Created by 李恒 on 2020/7/1.
//
#include <cstring>
#include <iostream>
#include <vector>

using  namespace std;
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        int sz = s.size();
        vector<vector<bool>> dp(sz, vector<bool>(sz, false));
        for(int i=0; i<sz; ++i){
            for(int j=i; j>=0; j--){
                if(s[i]==s[j] && ((i-j)<2 || dp[j+1][i-1]))
                    dp[j][i] = true; //注意是dp[j][i] 不是dp[i][j]
            }
        }
        vector<string> tmp;
        dfs(res, dp, 0, s, tmp);
        return res;

    }

    void dfs(vector<vector<string>>& res, vector<vector<bool>> dp, int start, string s, vector<string>& tmp  ){
        if(start == s.size()) res.push_back(tmp);
        for(int j=start; j<s.size(); ++j){
            if(dp[start][j]){
                tmp.push_back(s.substr(start, j-start+1));
                dfs(res, dp, j+1, s, tmp);
                tmp.pop_back();
            }
        }
    }

};