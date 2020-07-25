//
// Created by 李恒 on 2020/1/9.
//

//螺旋矩阵II


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // 创建二维矩阵
        vector<vector<int>> matrix(n);
        for (int i = 0; i < matrix.size(); i++)
            matrix[i].resize(n);

        // 上下左右
        int u = 0;
        int d = n-1;
        int l = 0;
        int r = n-1;
        int num = 1;

        while(true){
            // 上边界
            for(int i=l; i <= r; i++) matrix[u][i] = num++;
            //注意u++ 只是u自增了，整个表达式的值是u之前的值
            if (u++ >= d) break; //转向时候 ↓ 移一位不越界
            // 右边界
            for(int i=u; i <= d; i++) matrix[i][r] = num++;
            if (r-- <= l) break; //转向时候 ← 移一位不越界
            // 下边界
            for(int i=r; i >= l; i--) matrix[d][i] = num++;
            if (d-- <= u) break; //转向时候 ↑ 移一位不越界
            // 左边界
            for(int i=d; i >= u; i--) matrix[i][l] = num++;
            if (l++ >= r) break; //转向时候 → 移一位不越界
        }
        return matrix;
    }
};



class Solution1 {
public:
    vector<vector<int>> generateMatrix(int n) {
        // 创建二维矩阵
        vector<vector<int>> matrix(n);
        for (int i = 0; i < matrix.size(); i++)
            matrix[i].resize(n);
        // 上下左右
        int u = 0;
        int d = n-1;
        int l = 0;
        int r = n-1;
        int num = 1;

        while(true){
            // 上边界
            for(int i=l; i <= r; i++) matrix[u][i] = num++;
            //if (u++ >= d) break; //转向时候 ↓ 移一位不越界
            if(u >= d) break;
            u = u + 1;
            // 右边界
            for(int i=u; i <= d; i++) matrix[i][r] = num++;
            //if (r-- <= l) break; //转向时候 ← 移一位不越界
            if(r <= l ) break;
            r =  r - 1;
            // 下边界
            for(int i=r; i >= l; i--) matrix[d][i] = num++;
            //if (d-- <= u) break; //转向时候 ↑ 移一位不越界
            if(d <= u) break;
            d = d - 1;
            // 左边界
            for(int i=d; i >= u; i--) matrix[i][l] = num++;
            //if (l++ >= r) break; //转向时候 → 移一位不越界
            if(l >= r) break ;
            l = l + 1 ;
        }
        return matrix;
    }
};



int main(){
    vector<vector<int>> ma = Solution1().generateMatrix(2);
    cout << ma.size()<<endl;
    cout << ma[1].size()<<endl;
    cout << ma[1][1]<<endl;
}