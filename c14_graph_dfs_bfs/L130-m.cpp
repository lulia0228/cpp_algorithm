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

//仍然可以看成是回溯的思路，下探的层数不固定，每层的迭代对象是4个方向的判定条件
//总结：回溯写法要搞清楚2点：1 下探层数（可能是固定，也可能是不固定，依据此设计递归中止条件）2 每一层迭代的是哪些对象

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
        //1  if(!visited[startx][starty]) 就可以了，不需要判断board[startx][starty] == 'O'
        //2  后来发现因为走过的被置为'#"回退后根本不用担心走老路，所以可以不设置visited数组
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




// 2 设计显式栈，每个方向的代码块里必须要有continue这句话，此外因为凡是走过的位置都变成了'#"，
// 因此当退回去之后，当前方向就不会再走了，不会因为continue导致不能执行别的方向
#include <stack>
class Solution1 {
public:
    void solve(vector<vector<char>>& board) {
        if (board.size() == 0) return;
        int m = board.size();
        int n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 只对边缘有O的做特殊处理
                bool isEdge = (i == 0 || j == 0 || i == m - 1 || j == n - 1);
                if (isEdge && board[i][j] == 'O') {
                    dfs(board, i, j);
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    void dfs(vector<vector<char>>& board, int i, int j) {
        stack<pair<int,int>> stk;
        stk.push(make_pair(i, j));
        board[i][j] = '#';
        while (!stk.empty()) {
            // 取出当前stack 顶, 不弹出.
            pair<int,int> current = stk.top();
            // 上
            if (current.first - 1 >= 0
                && board[current.first - 1][current.second] == 'O') {
                stk.push(make_pair(current.first - 1, current.second));
                board[current.first - 1][current.second] = '#';
                continue;
            }
            // 下
            if (current.first + 1 <= board.size() - 1
                && board[current.first + 1][current.second] == 'O') {
                stk.push(make_pair(current.first + 1, current.second));
                board[current.first + 1][current.second] = '#';
                continue;
            }
            // 左
            if (current.second - 1 >= 0
                && board[current.first][current.second - 1] == 'O') {
                stk.push(make_pair(current.first, current.second - 1));
                board[current.first][current.second - 1] = '#';
                continue;
            }
            // 右
            if (current.second + 1 <= board[0].size() - 1
                && board[current.first][current.second + 1] == 'O') {
                stk.push(make_pair(current.first, current.second + 1));
                board[current.first][current.second + 1] = '#';
                continue;
            }
            // 如果上下左右都搜索不到,本次搜索结束，弹出stack
            stk.pop();
        }
    }

};
