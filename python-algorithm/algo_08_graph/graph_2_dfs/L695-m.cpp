//
// Created by LiHeng on 2020/7/12.
//

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
class Solution{
private:
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;
    int m, n ;

    int dfs(vector<vector<int>>& grid, int x ,int y){
        if(grid[x][y] != 1)
            return 0;
        grid[x][y] = 0 ; //不会走重复路径
        int area = 1;
        for(int i = 0 ; i < 4 ; i++){
            int newx = x + d[i][0] ;
            int newy = y + d[i][1] ;
            if(newx>=0 && newx<m && newy>=0 && newy<n)
                area += dfs(grid, newx, newy);
        }
        return area;
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid){
        m = grid.size() ;
        if(m == 0)
            return 0;
        n = grid[0].size() ;
        int res = 0 ;
        for(int i = 0 ; i < m ; ++i)
            for(int j = 0 ; j < n; ++j)
                if(grid[i][j] == 1){
                    res = max(res, dfs(grid , i , j));
                }
        return res ;
    }
};

//也可以下面这样写
class Solution1{
private:
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;
    int m , n ;
    vector<vector<bool>> vistited;


    int dfs(vector<vector<int>>& grid, int x ,int y){
        if(grid[x][y] != 1)
            return 0;
        vistited[x][y] = true ; //不会走重复路径
        int area = 1;
        for(int i = 0 ; i < 4 ; i++){
            int newx = x + d[i][0] ;
            int newy = y + d[i][1] ;
            if(newx>=0 && newx<m && newy>=0 && newy<n && !vistited[newx][newy])
                area += dfs(grid, newx, newy);
        }
        return area;
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid){
        m = grid.size() ;
        if(m == 0)
            return 0;
        n = grid[0].size() ;
        int res = 0 ;
        vistited = vector<vector<bool>> (m, vector<bool>(n, false));
        for(int i = 0 ; i < m ; ++i)
            for(int j = 0 ; j < n; ++j)
                if(grid[i][j] == 1 && !vistited[i][j]){
                    res = max(res, dfs(grid , i , j));
                }
        return res ;
    }
};