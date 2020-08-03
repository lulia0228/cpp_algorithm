//
// Created by LiHeng on 2020/4/28.
//
#include <iostream>
#include <cstring>
#include <vector>
using namespace std ;

//方法1 遍历到每个元素，对每个元素使用中心扩展，中心扩展包括奇数和偶数长度两种情况
//这样最快
class Solution {
public:
    int countSubstrings(string s) {
        int ans = 0;
        int len = s.size();
        for (int i = 0; i < len; i++) {
            ans++;
            int l = i - 1, r = i + 1;
            while (l >= 0 && r < len && s[l] == s[r]) {//奇数长度
                ans++;
                l--;
                r++;
            }
            l = i - 1, r = i;
            while (l >= 0 && r < len && s[l] == s[r]) {//偶数长度
                ans++;
                l--;
                r++;
            }
        }
        return ans;

    }
};

//方法2 DP实现
//思路可以参考leetcode第5题
//使用动态规划， dp[j][i] 代表s[j:i]是否是回文子串
//考虑单字符和双字符的特殊情况
//状态转移方程：dp[j][i] = dp[j+1][i-1] && str[j]== str[i]

//当时这道题这么做，又不像是DP ？因为还遍历，是对每个遍历的元素使用DP
class Solution1 {
public:
    int countSubstrings(string s) {
        int res = 0;
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false)); //只有上三角阵有用
        for(int i = 0; i < s.size(); i++){ //即每次遍历以当前元素作为回文串最后一个值
            for(int j = i; j >= 0; j--){
                if(s[j] == s[i] && ((i - j) < 2 || dp[j+1][i-1])){
                    dp[j][i] = true;
                    res++;
                }
            }
        }
        return res;
    }
};

//空间复杂度从n*n 降到2*n
class Solution2 {
public:
    int countSubstrings(string s) {
        int res = 0;
        vector<bool> tmp(s.size(),  false);
        for(int i = 0; i < s.size(); i++){
            vector<bool> dp(s.size(),  false); //每次循环在开辟一个数组存储以s[i]结尾的回文串情况
            for(int j = i; j >= 0; j--){
                if(s[j] == s[i] && ((i - j) < 2 || tmp[j+1])){//下一次遍历要用到上一次的结果
                    dp[j] = true;
                    res++;
                }
            }
            tmp = dp;//不上一次的结果存储下来作为下一次使用
        }
        return res;
    }
};


int main(){
    string s1 = "aaaaa";
//    string s1 = "aba";
    int res =  Solution1().countSubstrings(s1);
    cout << res << endl;
    return 0;
}