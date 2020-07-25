//
// Created by LiHeng on 2020/6/21.
//

//这道题转化成求最长公共子序列问题，参考1143
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size() ;
        int n = word2.size() ;
        int longest = 0 ;
        vector<vector<int>> memo(m+1 ,vector<int> (n+1,0));
        //memo[0][0]存储的是2个字符串中都没有字符的状态
        //memo[i][j]代表word1[0:i) word2[0:j) 两个字符串的最长公共子序列
        for(int i=1 ; i < m+1 ; i++){
            for(int j = 1 ; j < n+1 ;j++){
                if(word1[i-1] == word2[j-1]){
                    memo[i][j] = memo[i-1][j-1] + 1 ;
                }
                else
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1]) ;
            }
        }
        return m+n-2*memo[m][n];
    }
};