
//leetcode 200 number of islands 解决办法：图的深度遍历

#include <iostream>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std ;
class Solution{
private:
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;
    int m , n ;
    vector<vector<bool>> visited ;

    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }

    //从grid[x][y]位置运行floodfill
    //
    void dfs(vector<vector<char>>& grid , int x ,int y){
        visited[x][y] = true ;
        //这里似乎没有看到递归终止条件，是因为包含在下面的条件判断语句中了
        for(int i = 0 ; i < 4 ; i++){
            int newx = x + d[i][0] ;
            int newy = y + d[i][1] ;
            if(inArea(newx, newy) && !visited[newx][newy] && grid[newx][newy]=='1')
                dfs(grid, newx, newy);
        }
        return;
    }

public:
    int numIslands(vector<vector<char>>& grid){
        m = grid.size() ;
        if(m == 0 )
            return 0;
        n = grid[0].size() ;
        visited = vector<vector<bool>> (m , vector<bool>(n , false));
        int res = 0 ;
        for(int i = 0 ; i < m ; i ++)
            for(int j = 0 ; j < grid[i].size() ; j ++)
                if(grid[i][j] == '1' && !visited[i][j]){
                    res++;
                    dfs(grid , i , j );
                }
        return res ;
    }
};

//下面的写法更简洁
class Solution1{
private:
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;
    int m , n ;


    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }

    //从grid[x][y]位置运行floodfill
    void dfs(vector<vector<char>>& grid , int x ,int y){
        if(grid[x][y] != '1')
            return;
        grid[x][y] = '0' ; //不会走重复路径
        for(int i = 0 ; i < 4 ; i++){
            int newx = x + d[i][0] ;
            int newy = y + d[i][1] ;
            if(inArea(newx, newy))
                dfs(grid, newx, newy);
        }
        return;
    }

public:
    int numIslands(vector<vector<char>>& grid){
        m = grid.size() ;
        if(m == 0 )
            return 0;
        n = grid[0].size() ;
        int res = 0 ;
        for(int i = 0 ; i < m ; i ++)
            for(int j = 0 ; j < grid[i].size() ; j ++)
                if(grid[i][j] == '1'){
                    ++res;
                    dfs(grid , i , j );
                }
        return res ;
    }
};