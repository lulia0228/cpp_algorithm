//
// Created by LiHeng on 2019/8/10.
//
// 深度优先搜索和广度优先搜索广泛运用于树和图中

// BFS:广度优先搜索一层一层地进行遍历，每层遍历都是以上一层遍历的结果作为起点，
// 遍历一个距离能访问到的所有节点。需要注意的是，遍历过的节点不能再次被遍历。
// 设di表示第i个节点与根节点的距离，先遍历的节点i与后遍历的节点j，有 di <= dj。
// 利用这个结论，可以求解最短路径等最优解问题

//在程序实现 BFS 时需要考虑以下问题：
//    队列：用来存储每一轮遍历得到的节点,另外要设计队列存储元素的结构来储存节点所需要的信息
//    标记：对于遍历过的节点，应该将它标记，防止重复遍历。


//leetcode 279 看成一个图，转换成图中从n走到0的图的最短路径
#include <iostream>
#include <queue>
#include <vector>
#include <cassert>
#include <stdexcept>

//BFS: n->0
using namespace std ;
class Solution{
public:
    int numSquares(int n){
        assert(n > 0);
        queue< pair< int , int > > q ;
        q.push(make_pair(n , 0)); //后面一个代表到达n需要的步数

        vector<bool> visited(n + 1 , false) ;//设置一个访问记录数组，避免重复往队列推入数据
        //visited[n] = true ;

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
        //throw  invalid_argument("No Solution .") ;
        return 0;
    }
};

//BFS: 0->n
class Solution1{
public:
    int numSquares(int n){
        assert(n > 0);
        queue< pair< int , int > > q ;
        q.push(make_pair(0 , 0));

        vector<bool> visited(n + 1 , false) ;//设置一个访问记录数组，避免重复往队列推入数据
        //visited[0] = true ;

        while(!q.empty()){
            int num = q.front().first ;
            int step = q.front().second ;
            q.pop() ;
            for(int i = 1 ; num + i*i <= n ; i++){
                int a = num + i*i ;
                if ( a == n )
                    return step + 1 ;
                if (!visited[a]){
                    q.push(make_pair(a , step + 1)) ; //注意step还是step在while本轮循环的值 代表从n走到a的路径是（step+1）
                    visited[a] = true ;
                }
            }
        }
        //throw  invalid_argument("No Solution .") ;
        return 0 ;
    }
};

int main(){
    int num1 = 13 ;
    cout<<  Solution1().numSquares(num1);
}



//练习 leetcode 126 127