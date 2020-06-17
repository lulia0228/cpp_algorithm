//
// Created by LiHeng on 2020/4/22.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m= grid.size();
        int n= grid[0].size();
        vector<vector<int>> res(m,vector<int>(n,grid[0][0]));

        for(int i=1; i<n; i++)
            res[0][i] = grid[0][i] + res[0][i-1];
        for(int j=1; j<m; j++)
            res[j][0] = grid[j][0] + res[j-1][0];

        for(int row=1; row<m; row++){
            for (int col=1; col<n; col++)
                res[row][col] = min(res[row-1][col] , res[row][col-1]) + grid[row][col];
        }
        return res[m-1][n-1];
    }
};