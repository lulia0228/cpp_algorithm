//
// Created by LiHeng on 2019/8/10.
//
//BFS 和 图的最短路径

//leetcode 279 看成一个图，转换成图中从n走到0的图的最短路径
#include <iostream>
#include <queue>
#include <vector>
#include <cassert>
#include <stdexcept>

using namespace std ;
class Solution{
public:
    int numSquares(int n){
        assert(n > 0);
        queue< pair< int , int > > q ;
        q.push(make_pair(n , 0)); //后面一个代表到达

        vector<bool> visited(n + 1 , false) ;//设置一个访问记录数组，避免重复往队列推入数据
        visited[n] = true ;

        while(!q.empty()){
            int num = q.front().first ;
            int step = q.front().second ;
            q.pop() ;
            for(int i = 1 ; num - i*i >= 0 ; i++){
                int a = num - i*i ;
                if ( a == 0 )
                    return step + 1 ;
                if (!visited[a]){
                    q.push(make_pair(a , step + 1)) ; //注意step还是step在while本轮循环的值 代表从n走到a的路径是（step+1）
                    visited[a] = true ;
                }
            }
        }
        throw  invalid_argument("No Solution .") ;
    }
};

int main(){
    int num1 = 13 ;
    cout<<  Solution().numSquares(num1);
}

//注意代码也可以正向写成从0走到n ；有空可以改写一个

//练习 leetcode 127 126