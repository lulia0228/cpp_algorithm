//
// Created by LiHeng on 2020/5/22.
//

#include <iostream>
#include <cstring>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int sz1 = word1.size();
        int sz2 = word2.size();
        int dp[sz1+1][sz2+1];
        for(int i=0; i<=sz2; ++i)
            dp[0][i] = i; //word1添加i次
        for(int i=0; i<=sz1; ++i)
            dp[i][0] = i; //word1删除i次
        for(int i=1; i<=sz1; ++i)
            for(int j=1; j<=sz2; ++j){
                if(word1[i-1] == word2[j-1]) //下标有多重，注意别写错了 一开始j-1写成了i-1就报错
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
            }
        return dp[sz1][sz2];
    }
};

//优化了空间存储，即只使用2行  len(word1)*len(word2) 到2*len(word2)
class Solution1 {
public:
    int minDistance(string word1, string word2) {
        int sz1 = word1.size();
        int sz2 = word2.size();
        int dp[2][sz2+1];
        for(int i=0; i<=sz2; ++i)
            dp[0][i] = i; //word1添加i次

        for(int i=1; i<=sz1; ++i){
            for(int j=0; j<=sz2; ++j){
                if(j == 0){
                    dp[1][j] = i;
                    continue;
                }
                if(word1[i-1] == word2[j-1])
                    dp[1][j] = dp[0][j-1];
                else
                    dp[1][j] = min(min(dp[0][j], dp[1][j-1]), dp[0][j-1]) + 1;
            }
            for(int i=0; i<= sz2; ++i)
                dp[0][i] = dp[1][i];//这里不能对第一维度直接赋值即不能用dp[0]=dp[1]
        }
        return dp[0][sz2];
    }
};