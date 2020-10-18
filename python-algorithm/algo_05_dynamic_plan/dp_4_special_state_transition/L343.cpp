

//leetcode 343 最大乘积问题
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    int integerBreak(int n) {
        vector<int> memo(n+1 , -1) ;
        memo[1] = 1;
        for(int i = 2;i <= n ; i++)
            //求解memo[i]
            for(int j = 1 ; j < i ; j ++)
                memo[i] = max(memo[i] , max(j*(i-j) , j * memo[i-j]));
        return memo[n];
    }
};

class Solution1{
private:
    vector<int> memo ;
    int max3(int a , int b , int c){
        return max(a , max(b , c));
    }

    //将n进行分割(至少分割两部分) 自顶向下递归+记忆化搜索
    int breakInteger(int n){
        if ( n == 1)
            return 1;
        if (memo[n] != -1)
            return memo[n];
        int res = -1 ;
        for(int i = 1 ; i< n ; i++)
            res =  max3(res , i*(n - i) , i * breakInteger(n - i));
        memo[n] = res ;
        return res ;
    }
    
public:
    int integerBreak(int n ){
        assert(n > 1) ;
        memo = vector<int> (n+1 , -1) ;
        return breakInteger(n);
    }

    //DP自底向上
    int integerBreakDP(int n ){
        vector<int> memo(n+1 , -1) ;
        memo[1] = 1;
        for(int i = 2;i <= n ; i++)
            //求解memo[i]
            for(int j = 1 ; j < i ; j ++)
                memo[i] = max3(memo[i] , j*(i-j) , j * memo[i-j]);
        return memo[n];
    }

};


int main(){
    int n  =  10 ;
    cout << Solution().integerBreak(n)<<endl;
    cout << Solution1().integerBreakDP(n);
}


