

//螺旋矩阵

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int m = matrix.size();
        if(m == 0)
            return res;
        int n = matrix[0].size();

        // 上下左右
        int u = 0;
        int d = m-1;
        int l = 0;
        int r = n-1;
        int num = 1;

        while(true){
            // 上边界
            for(int i=l; i <= r; i++) res.push_back(matrix[u][i]);
            //if (u++ >= d) break; //转向时候 ↓ 移一位不越界
            if(u >= d) break;
            u = u + 1;
            // 右边界
            for(int i=u; i <= d; i++) res.push_back(matrix[i][r]);
            //if (r-- <= l) break; //转向时候 ← 移一位不越界
            if(r <= l ) break;
            r =  r - 1;
            // 下边界
            for(int i=r; i >= l; i--) res.push_back(matrix[d][i]);
            //if (d-- <= u) break; //转向时候 ↑ 移一位不越界
            if(d <= u) break;
            d = d - 1;
            // 左边界
            for(int i=d; i >= u; i--) res.push_back(matrix[i][l]);
            //if (l++ >= r) break; //转向时候 → 移一位不越界
            if(l >= r) break ;
            l = l + 1 ;
        }
        return res;
    }
};


int main(){
    return 0;
}