//
// Created by LiHeng on 2020/7/12.
//

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

//我写的  又臭又长
class Solution {
private:
    int m, n;
    int d[4][2] = {{0, 1},{1,0},{0,-1},{-1,0}} ;

    bool inArea(int x , int y){
        return x>=0 && x<m && y>=0 && y<n ;
    }
public:
    int findCircleNum(vector<vector<int>>& M) {
        int res = 0;
        m = M.size();
        if(m == 0) return res;
        n = M[0].size();
        for(int i=0; i<m; ++i){
            for(int j=i; j<n; ++j){
                cout << "*************"<<i<<j<<endl;
                if(M[i][j] == 1){
                    ++res;
                    dfs(M, i, j);
                }
            }
        }
        return res;
    }

    void dfs(vector<vector<int>>& M, int x, int y){
        if (M[x][y] != 1)
            return;
        M[x][y] = 0;
        cout << x << y << '\t'<<M[x][y]<< endl;
        for(int i = 1 ; i+y < n ; ++i){
            int newx = x ;
            int newy = y + i ;
            if(inArea(newx, newy))
                dfs(M, newx, newy);
        }
        for(int i = 1 ; i+x <= y ; ++i){
            int newx = x + i ;
            int newy = y  ;
            if(inArea(newx, newy))
                dfs(M, newx, newy);
        }
        for(int i = 1 ; y-i >= x ; ++i){
            int newx = x ;
            int newy = y - i ;
            if(inArea(newx, newy))
                dfs(M, newx, newy);
        }
        for(int i = 1 ; x-i >= 0 ; ++i){
            int newx = x - i ;
            int newy = y ;
            if(inArea(newx, newy))
                dfs(M, newx, newy);
        }
    }
};

//下面写的简洁点儿
class Solution1 {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int res = 0;
        int m = M.size();
        if(m == 0) return res;
        //标记第i个学生是否已经被访问了
        vector<bool> visited(m, false);
        for(int i=0; i<m; ++i){
            if(!visited[i]){
                ++res;
                dfs(M, visited, i);
            }
        }
        return res;
    }

    void dfs(vector<vector<int>>& M, vector<bool>& visited, int i){
        for (int j = 0; j < M.size(); ++j) {
            if (M[i][j] == 1 && !visited[j]) {
                visited[j] = true;
                dfs(M, visited, j);
            }
        }
    }

};

int main(){
    vector<vector<int>> m = {{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}};
    int res = Solution().findCircleNum(m);
    cout << res << endl;
}

