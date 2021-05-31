
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> pos;
    vector<vector<char>> res;
    void solveSudoku(vector<vector<char>>& board) {
        //初始化vector放在构造函数或者函数，不能直接在外面初始化
        vector<vector<int>> row(9, vector<int>(10,0));
        vector<vector<int>> col(9, vector<int>(10,0));
        vector<vector<int>> box(9, vector<int>(10,0));
        for(int i=0; i<9; ++i)
            for(int j=0; j<9; ++j){
                if(board[i][j] == '.')
                    pos.push_back(vector<int>{i,j});
                else{
                    int curNumber = board[i][j]-'0';
                    row[i][curNumber] = 1;
                    col[j][curNumber] = 1;
                    box[j/3 + (i/3)*3][curNumber] = 1;
                }
            }
        vector<char> cur;
        dfs(board, 0, cur, row, col, box);
        for(auto v:res){
            for(int i=0; i<v.size(); ++i)
                board[pos[i][0]][pos[i][1]] = v[i] ;
        }

    }

    void dfs(vector<vector<char>>& board, int idx, vector<char>& cur,
             vector<vector<int>>&row,vector<vector<int>>&col,vector<vector<int>>&box){
        if(idx == pos.size()){
            res.push_back(cur);
            return;
        }
        for(int num=1; num<=9; ++num){
            int t_r = pos[idx][0];
            int t_c = pos[idx][1];
            if(!row[t_r][num] && !col[t_c][num] && !box[t_c/3 + (t_r/3)*3][num]){
                char c = to_string(num)[0];
                cur.push_back(c);
                row[t_r][num] = 1;
                col[t_c][num] = 1;
                box[t_c/3 + (t_r/3)*3][num] = 1;
                dfs(board, idx+1, cur, row, col, box);
                cur.pop_back();
                row[t_r][num] = 0;
                col[t_c][num] = 0;
                box[t_c/3 + (t_r/3)*3][num] = 0;
            }
        }
    }
};


int main(){
    vector<vector<char>> b = {{'5','3','.','.','7','.','.','.','.'},
                              {'6','.','.','1','9','5','.','.','.'},
                              {'.','9','8','.','.','.','.','6','.'},
                              {'8','.','.','.','6','.','.','.','3'},
                              {'4','.','.','8','.','3','.','.','1'},
                              {'7','.','.','.','2','.','.','.','6'},
                              {'.','6','.','.','.','.','2','8','.'},
                              {'.','.','.','4','1','9','.','.','5'},
                              {'.','.','.','.','8','.','.','7','9'}};
    Solution().solveSudoku(b);
}