//
// Created by LiHeng on 2020/4/22.
//
/*
Backtracking（回溯）属于 DFS。

普通DFS主要用在可达性问题这种问题只需要执行到特点的位置然后返回即可。
    而Backtracking主要用于求解排列组合问题，例如有{'a','b','c' }三个字符求解所有由这三个字符排列得到的字符串，
    这种问题在执行到特定的位置返回之后还会继续执行求解过程。
    因为 Backtracking 不是立即返回，而要继续求解，因此在程序实现时，需要注意对元素的标记问题：

    在访问一个新元素进入新的递归调用时，需要将新元素标记为已经访问，这样才能在继续递归调用时不用重复访问该元素；
    但是在递归返回时，需要将元素标记为未访问，因为只需要保证在一个递归链中不同时访问一个元素，
    可以访问已经访问过但是不在当前递归链中的元素。
*/

// 单词搜索；回溯问题

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

class Solution {
public:
    //貌似真的是这里word传引用比传值要快10倍（时间和空间都快了）string& word > string word
    bool dfs(vector<vector<char>>& board, string& word, int i,int j, int index){
        if(board[i][j] != word[index])//当前考察字符不相等
            return false;
        if(index == word.length()-1) //走到最后一个字符还相等
            return true;
        char tmp = board[i][j];
        board[i][j] = '0'; //防止走回头路
        if( (i-1>=0 && dfs(board, word, i-1, j, index+1))
            || (j+1<=board[0].size()-1 && dfs(board, word, i, j+1, index+1))
            || (i+1<=board.size()-1 && dfs(board, word, i+1, j, index+1))
            || (j-1>=0 && dfs(board, word, i, j-1, index+1)) ) //有一条通，就算成功
            return true;
        board[i][j] = tmp;//都不通，就回溯到上一层
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++)
                if(dfs(board, word, i, j, 0))//从二维表格的每一个格子作为出发点
                    return true;
        }
        return false;
    }
};

//下面的代码量稍微多一些，但是思路一样
class Solution1 {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0; i<board.size(); i++)
            for(int j = 0; j<board[i].size(); j++) {
                bool rs = DFS(board,word,0,i,j);
                if(rs)
                    return true;
            }
        return false;
    }

private:
    bool DFS(vector<vector<char>>& board,string word,int index, int i, int j) {
        bool rs = false;
        //判断这个点对不对
        if(word[index] != board[i][j])
            return false;
        //判断到没到头
        if(index == word.size()-1)
            return true;

        char tmp = board[i][j];
        //临时变量替换 防止 回头路
        board[i][j] = '0';

        //判断向上走
        if(i-1 >=0 ) {
            rs = DFS(board, word, index+1, i-1, j);
            if(rs) return true;
        }

        //判断向右走
        if(j+1 < board[0].size()) {
            rs = DFS(board, word, index+1, i, j+1);
            if(rs) return true;
        }

        //判断向下走
        if( i+1 < board.size()) {
            rs = DFS(board, word, index+1, i+1, j);
            if(rs) return true;
        }

        //判断向左走
        if(j-1 >= 0) {
            rs = DFS(board,word,index+1,i,j-1);
            if(rs) return true;
        }

        board[i][j] = tmp;
        return rs;
    }
};

class Solution2{
private:
    int d[4][2] = {{-1,0},{0, 1},{1,0},{0,-1}} ;
    int m , n ;
    vector<vector<bool>> visited ;

    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }

    //从board[startx][starty]开始寻找word[index...word.size()]
    bool searchWord(const vector<vector<char>> &board , const string &word , int index ,
                    int startx , int starty){
        if(index == word.size()-1)
            return board[startx][starty] == word[index] ;

        if(board[startx][starty] == word[index]) {
            visited[startx][starty] = true ;
            //从[startx][starty]出发，4个方向寻找
            for(int i = 0 ; i < 4 ; i++){
                int newx = startx+d[i][0];
                int newy = starty+d[i][1];
                if(inArea(newx,newy) && !visited[newx][newy] && searchWord(board,word,index+1,newx,newy))
                    return true ;
            }
            visited[startx][starty] = false ;
        }
        return false ;
    }

public:
    bool exist(vector<vector<char>>& board , string word ){
        m = board.size() ;
        n = board[0].size();
        visited = vector<vector<bool>> (m, vector<bool>(n, false));
        for(int i = 0 ; i < m ; i ++)
            for(int j = 0 ; j < board[i].size() ; j ++)
                if(searchWord(board , word , 0 , i , j))
                    return true ;
        return false;
    }

};




