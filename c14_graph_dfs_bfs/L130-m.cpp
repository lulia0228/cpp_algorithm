//
// Created by LiHeng on 2020/7/5.
//


//从一个节点出发，使用 DFS 对一个图进行遍历时，能够遍历到的节点都是从初始节点可达的，DFS 常用来求解这种 可达性 问题。
//在程序实现 DFS 时需要考虑以下问题：
//    栈：用栈来保存当前节点信息，当遍历新节点返回时能够继续遍历当前节点。可以使用递归栈。
//    标记：和 BFS 一样同样需要对已经遍历过的节点进行标记。


// 这道题转化成了找到所有和边界为’O‘的元素的连通区域，这些区域是不能被更改成’X'的.

// 下面的解法仿照L79 visited数组作用类似之前写回溯算法中的当前记录数组的作用，
// 即发挥栈的作用，只是用了bool来作用，没有用压入弹出操作注意区别

#include <iostream>
#include <vector>
using namespace std;
class Solution{
private:
    int d[4][2] = {{-1,0},{0, 1},{1,0},{0,-1}} ;
    int m,n; //因为inArea里面用到了
    vector<vector<bool>> visited ;

    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }

    void dfs(vector<vector<char>> &board,  int startx, int starty){
        if(board[startx][starty] != 'O')
            return;
        //if(!visited[startx][starty]) 就可以了，不需要判断board[startx][starty] == 'O'
        if(board[startx][starty] == 'O' && !visited[startx][starty]) {
            visited[startx][starty] = true ;
            board[startx][starty] = '#';
            //从[startx][starty]出发，4个方向寻找
            for(int i = 0 ; i < 4 ; i++){
                int newx = startx+d[i][0];
                int newy = starty+d[i][1];
                if(inArea(newx,newy))
                    dfs(board, newx, newy);
            }
            visited[startx][starty] = false ;
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        m = board.size() ;
        if (m == 0) return;
        n = board[0].size();
        visited = vector<vector<bool>> (m, vector<bool>(n, false));
        for(int i=0 ; i<m ; ++i)
            for(int j=0 ; j<board[i].size() ; ++j) {
                bool isEdge = (i == 0 || j == 0 || i == m - 1 || j == n - 1);
                if(isEdge && board[i][j] == 'O')
                    dfs(board,i,j);
            }
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }

    }

};
