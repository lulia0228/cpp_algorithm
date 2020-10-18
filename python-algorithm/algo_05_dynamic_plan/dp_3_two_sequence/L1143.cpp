

//最长公共子序列L1143 字符串
#include <iostream>
#include <cstring>
#include <vector>
#include <stack>
#include <cmath>
#include <cassert>

using namespace std ;
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size() ;
        int n = text2.size() ;
        int longest = 0 ;
        vector<vector<int>> memo(m+1 ,vector<int> (n+1,0));
        //memo[0][0]存储的是2个字符串中都没有字符的状态
        //memo[i][j]代表text1[0:i) text2[0:j) 两个字符串的最长公共子序列
        for(int i=1 ; i < m+1 ; i++){
            for(int j = 1 ; j < n+1 ;j++){
                if(text1[i-1] == text2[j-1]){
                    memo[i][j] = memo[i-1][j-1] + 1 ;
                }
                else
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1]) ;
            }
        }
        return memo[m][n];
    }
};



class Solution1{
private:
    //flag[i][j] 存储 s1[0,...,i] s2[0,...,j] 二者的最长公共子序列值
    vector<vector<int>> flag ; //flag[0][0]表示的是2个字符串中都只有1个字符的意思
    int Lcs(string s1 , string s2 , int m , int n){
        //递归终止条件必须设立
        if( m == -1 || n == -1)
            return 0 ;
        if(flag[m][n] != -1)
            return flag[m][n];
        int tem ;
        if(s1[m] == s2[n])
            tem = Lcs(s1, s2, m-1, n-1) + 1 ;
        else
            tem = max(Lcs(s1, s2 , m-1 , n) , Lcs(s1, s2 , m , n-1 ) );
        flag[m][n] = tem ;
        return tem ;
    }

public:
    //记忆化搜索递归方式解决
    int LCS(string s1, string s2 ){
        int m = s1.length() ;
        int n = s2.length() ;
        flag = vector<vector<int>> ( m  , vector<int>(n , -1) );
        return Lcs(s1 ,s2 , m-1 , n-1) ;
    }

    //动态规划 自底向上解决
    int LCS_DP(string s1 , string s2){
        int m = s1.length() ;
        int n = s2.length() ;
        //这里memo[0][0]存储的是2个字符串中都没有字符的状态
        vector<vector<int>> memo( m+1  , vector<int>(n+1 , -1) ); //注意尺寸是(m+1)*(n+1)最大索引是（m,n)
        for(int i = 0 ; i <= n ; i++) //初始化S1中没有字符
            memo[0][i] = 0;
        for(int j = 1 ; j <= m ; j++)//初始化S2中没有字符
            memo[j][0] = 0;
        for(int i = 1 ; i <= m ; i++){
            for(int j = 1 ; j <= n ; j++){
                if(s1[i-1] == s2[j-1]) //是判断各有1个字符的情况
                    memo[i][j] = memo[i-1][j-1] + 1 ;
                else{
                    memo[i][j] = max(memo[i-1][j] , memo[i][j-1]);
                }
            }
        }
        return memo[m][n];
    }


};

//动态规划 自底向上解决 要求返回实际序列
class Solution2{
public:
    void LCS_DP(string s1 , string s2){
        int m = s1.length() ;
        int n = s2.length() ;
        vector<vector<int>> memo( m+1  , vector<int>(n+1 , -1) );
        vector<vector<int>> path( m+1  , vector<int>(n+1 , -1) );
        //因为这里memo[0][0]存储的是2个字符串中都没有字符的情况，所以遍历做判断要注意获取正确的索引

        for(int i = 0 ; i <= n ; i++) //初始化S1中米有字符
            memo[0][i] = 0;
        for(int j = 1 ; j <= m ; j++)//初始化S2中米有字符
            memo[j][0] = 0;
        for(int i = 1 ; i <= m ; i++){
            for(int j = 1 ; j <= n ; j++){
                if(s1[i-1] == s2[j-1]){   //是判断各有1个字符的情况
                    memo[i][j] = memo[i-1][j-1] + 1 ;
                    path[i][j] = 1 ;
                }
                else{
                    if(memo[i-1][j] >= memo[i][j-1]){
                        memo[i][j] = memo[i-1][j] ;
                        path[i][j] = 2 ;
                    }
                    else{
                        memo[i][j] = memo[i][j-1] ;
                        path[i][j] = 3 ;
                    }
                }
            }
        }
        cout<< "Max Length : " << memo[m][n] << endl;

        stack<char> stack1;
        while(m>0 && n>0){
            if(path[m][n] == 1){
                stack1.push(s1[m-1]);
                m--;
                n--;
            }
            else if(path[m][n] == 2)
                m--;
            else
                n--;
        }
        string res = "" ;
        while(!stack1.empty()){
            res += stack1.top() ;
            stack1.pop();
        }
        cout << "Real SubSequence is :" << res << endl ;
    }

};

int main(){
    string string1 = "ABCD" ;
    string string2 = "AEBD" ;
    int maxL = Solution1().LCS(string1 , string2);
    cout << maxL << endl ;
    int maxL2 = Solution1().LCS_DP(string1 , string2);
    cout << maxL2 << endl ;
    Solution1().LCS_DP(string1 , string2);
}

//dijkstra单源最短路径算法也是动态规划
