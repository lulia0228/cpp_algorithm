//
// Created by LiHeng on 2019/8/25.
//

//0-1背包 重点研究，此外如果需要返回实际装的物品，还需要记录下来路径
#include <iostream>
#include <vector>
#include <cassert>
using namespace std ;
class Solution{
private:
    vector<vector<int>> memo ; //状态标志
    // 用[0,...,index]的物品填充容量为c额背包的最大价值
    int bestValue(const vector<int>& w , const vector<int>& v , int index , int c){
        if(index < 0 || c <= 0 )
            return 0;
        if(memo[index][c] != -1)
            return memo[index][c];
        //不装第index 进去
        int res = bestValue(w , v , index- 1 , c);
        //装第index进去
        if(c >= w[index]){
            res =  max(res , v[index]+ bestValue(w , v , index-1 , c - w[index]) );
        }
        memo[index][c] = res ;
        return res ;
    }
public:
    //记忆化搜索 自顶向下 递归写法
    int knapsack01(const vector<int>& w , const vector<int>& v , int C){
        int n = w.size() ;
        memo = vector<vector<int>> (n , vector<int> (C+1, -1));
        return  bestValue(w , v , n-1 , C);
    }

    // 自底向上 动态规划写法
    int knapsack02(const vector<int> & w , const vector<int>& v , int C ){
        assert(w.size() == v.size()) ;
        int n = w.size() ;
        // stats[i][j]表示用[0,...,i]物品填充容量为j 的最大价值
        vector<vector<int>> stats(n , vector<int>( C+1 , -1)) ;
        //初始转态
        for(int j = 0 ; j <= C ; j ++)
            stats[0][j] = (j > w[0] ? v[0]: 0) ; //即考虑第1个物品（索引是0）各个重量下的转态
        for(int i = 1 ; i < n ; i ++)
            for(int j  = 0 ; j <= C ; j ++){
                stats[i][j] = stats[i-1][j]; //先给其赋值不装第index的状态
                if(j >= w[i])
                    stats[i][j] = max(stats[i][j], v[i]+stats[i-1][j - w[i]]);
            }
        return stats[n-1][C];
    }

    //优化空间存储 ，观察状态转移方程，发现每次只用到上一行的状态， 因此只用2行存储
    int knapsack03(const vector<int> & w , const vector<int>& v , int C ){
        assert(w.size() == v.size()) ;
        int n = w.size() ;
        // stats[i][j]表示用[0,...,i]物品填充容量为j 的最大价值
        vector<vector<int>> stats(2 , vector<int>( C+1 , -1)) ;
        //初始转态
        for(int j = 0 ; j <= C ; j ++)
            stats[0][j] = (j > w[0] ? v[0]: 0) ; //即考虑第1个物品（索引是0）各个重量下的转态
        for(int i = 1 ; i < n ; i ++)
            for(int j  = 0 ; j <= C ; j ++){
                stats[i%2][j] = stats[(i-1)%2][j];
                if(j >= w[i])
                    stats[i%2][j] = max(stats[i%2][j], v[i]+stats[(i-1)%2][j - w[i]]);
            }
        return stats[(n-1)%2][C];
    }

};

int main(){
    return  0 ;
}