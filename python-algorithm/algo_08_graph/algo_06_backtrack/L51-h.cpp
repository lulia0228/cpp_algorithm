
//八皇后问题L51

//带循环的递归，注意皇后问题51和全排列46、组合77这3道题目问题对比

#include <iostream>
#include <cassert>
#include <vector>
#include <cstring>

using namespace std ;
class Solution{
private:
    vector<vector<string>> res;
    vector<bool> col , dia1 ,  dia2 ;
    // 尝试在一个N皇后问题中，摆放第index行皇后的位置
    void pushQueen(int n , int index , vector<int>& row){
        //递归终止条件
        if(index == n ){
            res.push_back(generateBoard(n , row));
            return;
        }
        for (int i = 0 ; i < n ; i++)
            //尝试将第index行皇后摆放在第i列
            if(!col[i] && !dia1[index + i] && !dia2[index - i + n - 1]){
                row.push_back(i) ;
                col[i] = true ;
                dia1[index + i] = true ;
                dia2[index - i + n - 1] = true ;
                pushQueen(n , index+1 , row);
                row.pop_back() ;
                col[i] = false ;
                dia1[index + i] = false ;
                dia2[index - i + n - 1] = false ;
            }
    }

    vector<string> generateBoard(int n , vector<int> &row){
        assert(row.size() == n) ;
        vector<string> board( n , string( n , '.'));
        for(int i = 0 ; i < n ; i++)
            board[i][row[i]] = 'Q';
        return board ;
    }

public:
    vector<vector<string>> solveNQueens(int n){
        res.clear() ;
        col = vector<bool> (n , false) ;
        dia1 = vector<bool> (2*n-1 , false) ; //正对角线有2n-1条 且横纵坐标相加值相同
        dia2 = vector<bool> (n*n-1 , false) ; //副对角线有2n-1条
        vector<int> row ;
        pushQueen(n , 0 , row);
        return res ;
    }
};


int main(){
    int n = 8 ;
    int nums = 0  ;
    vector<vector<string>> re =  Solution().solveNQueens(n) ;
    for(int i = 0 ; i < re.size() ; i++){
        for(int j = 0 ; j < re[i].size() ; j ++)
            cout << re[i][j]<< "\t";
        nums += 1 ;
        cout << endl ;
    }
    cout << "摆放方法数： " << nums ;
}


//四皇后问题返回值如下：
//res = [[".Q.." , "...Q" , "Q..." , "..Q."] ,
//       ["..Q." , "Q..." , "...Q" , ".Q.."]]


//练习题 leetcode 52 37（数独）