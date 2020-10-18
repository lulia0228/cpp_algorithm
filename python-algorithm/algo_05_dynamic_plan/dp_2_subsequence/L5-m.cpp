
//最长回文子串

//动态规划解法
/*
解题思想：
dp[i,j] = 0/1 代表字符串s的下标从i到j的子串是不是回文串
如果 s[i]=s[j] 则有 dp[i,j] = dp[i+1,j-1]
如果 s[i]≠s[j] 则有 dp[i,j] = 0

意思是当s[i]=s[j]时，如果子字符串 是/不是 回文串，则在其两端各往外加一个字符后，整个字符串也 是/不是 回文串

*/
#include <iostream>
#include <cstring>
#include <vector>
using namespace std ;

class Solution {
public:
    string longestPalindrome(string s) {
        int len=s.size();
        if(len==0||len==1)
            return s;
        int start=0;//回文串起始位置
        int max=1;//回文串最大长度
        vector<vector<int>>  dp(len,vector<int>(len));//定义二维动态数组
        for(int i=0;i<len;i++)//初始化状态
        {
            dp[i][i]=1;
            if(i<len-1&&s[i]==s[i+1])
            {
                dp[i][i+1]=1;
                max=2;
                start=i;
            }
        }
        for(int l=3;l<=len;l++)//l表示检索的子串长度，等于3表示先检索长度为3的子串
        {
            for(int i=0;i+l-1<len;i++)
            {
                int j=l+i-1;//终止字符位置
                if(s[i]==s[j]&&dp[i+1][j-1]==1)//状态转移
                {
                    dp[i][j]=1;
                    start=i;
                    max=l;
                }
            }
        }
        return s.substr(start,max);//获取最长回文子串
    }
};

//我写的
class Solution1 {
public:
    string longestPalindrome(string s) {
        int sz = s.size();
        if(sz==0 || sz==1)
            return s;
        int max_len = 1;
        int min_start = 0;
        vector<vector<bool>> dp(sz, vector<bool>(sz, false));
        for(int i=0; i<s.size(); ++i){
            int cur_start = i; //标记以当前元素结尾的最长回文子串的起始位置
            int j = i;
            while(j>=0){
                if(s[j] == s[i] && (i-j<2 || dp[j+1][i-1])){
                    dp[j][i] = true;
                    cur_start = j;
                }
                --j;
            }
            if(i-cur_start+1 > max_len){
                max_len = i-cur_start+1;
                min_start = cur_start;
            }
        }
        return s.substr(min_start, max_len);
    }
};

//另外方法 参考L647