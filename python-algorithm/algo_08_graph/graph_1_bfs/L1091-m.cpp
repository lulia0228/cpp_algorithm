
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
//BFS时间效率上不去不知道为啥
class Solution {
public:
    int d[8][2]= {{1, -1}, {1, 0}, {1, 1}, {0, -1}, {0, 1}, {-1, -1}, {-1, 0}, {-1, 1}};
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(m == 0 || grid[0][0] == 1 || grid[m-1][n-1] == 1)
            return -1;
        queue<pair<int,int>> q;
        q.push(make_pair(0, 0));
        int path = 0;
        while(!q.empty()){
            int sz = q.size();
            ++path;
            for(int i=0; i<sz; ++i){
                int x = q.front().first;
                int y = q.front().second;
                q.pop();
                if (grid[x][y] == 1)
                    continue;
                if(x == m-1 && y == n-1)
                    return path;
                grid[x][y] = 1 ;  //标记,不走回头路
                for(int k=0; k<8; ++k){
                    int newx = x + d[k][0] ;
                    int newy = y + d[k][1] ;
                    if(newx<0||newx>=m||newy<0||newy>=n)
                        continue;
                    q.push(make_pair(newx, newy));
                }
            }
        }
        return -1;
    }
};
