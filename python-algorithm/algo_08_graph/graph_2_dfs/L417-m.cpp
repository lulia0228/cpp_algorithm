//
// Created by LiHeng on 2020/7/11.
//
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

//这道题多和130题对比下看看区别

class Solution {
private:
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;
    int m , n ;

    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<vector<int>> res;
        m = matrix.size();
        if (m == 0) return res;
        n = matrix[0].size();
        vector<vector<bool>> arrive_Pc(m, vector<bool>(n, false));
        vector<vector<bool>> arrive_At(m, vector<bool>(n, false));

        //即从边界出发，看看能到哪些位置
        for(int j=0; j<n; ++j) //找到与左边界连通的地方
            dfs(matrix, 0, j, arrive_Pc);
        for(int i=0; i<m; ++i) //找到与上边界连通的地方
            dfs(matrix, i, 0, arrive_Pc);

        for(int j=0; j<n; ++j) //找到与下边界连通的地方
            dfs(matrix, m-1, j, arrive_At);
        for(int i=0; i<m; ++i) //找到与右边界连通的地方
            dfs(matrix, i, n-1, arrive_At);

        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(arrive_Pc[i][j] && arrive_At[i][j])
                    res.push_back(vector<int>{i,j});
            }
        }
        return res;
    }

    void dfs(vector<vector<int>>& matrix, int i, int j, vector<vector<bool>>& visited ){
        if (visited[i][j])
            return;
        visited[i][j] = true;
        for(int k = 0 ; k < 4 ; k++){
            int newx = i + d[k][0] ;
            int newy = j + d[k][1] ;
            if(inArea(newx, newy) && matrix[newx][newy] >= matrix[i][j])
                dfs(matrix, newx, newy, visited);
        }
        // if (!visited[i][j]){
        //     visited[i][j] = true;
        //     for(int k = 0 ; k < 4 ; k++){
        //         int newx = i + d[k][0] ;
        //         int newy = j + d[k][1] ;
        //         if(inArea(newx, newy) && matrix[newx][newy] >= matrix[i][j])
        //             dfs(matrix, newx, newy, visited);
        //     }
        // }
    }

};

int main(){
    vector<vector<int>> v = {{1,2,3,4,5},
                             {16,17,18,19,6},
                             {15,24,25,20,7},
                             {14,23,22,21,8},
                             {13,12,11,10,9}};
    vector<vector<int>> res = Solution().pacificAtlantic(v);
    for(auto i:res){
        for(auto j:i)
            cout << j << '\t' ;
        cout << endl;
    }

}