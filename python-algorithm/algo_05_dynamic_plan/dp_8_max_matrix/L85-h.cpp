
// 这道题用dp做，时空复杂度不理想；还有一种方法转化成了单调栈还没去看？？？
#include <iostream>
#include <vector>
using namespace std;

//dp[i][j]存储的是以matrix[i][j]作为矩阵右下角的矩形的信息，包含三个参数。
//第一个表示该矩阵在行上向左有几个连续1（从本身开始计数）
//第二个表示该矩阵在列上向上有几个连续1（从本身开始计数）
//第三个参数表示的是以matrix[i][j]作为矩阵右下角的最大矩形面积

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if(m == 0)
            return 0;
        int n = matrix[0].size();
        int ans = 0;
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, {0,0,0}));
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++){
                if (matrix[i][j] == '0')
                    continue;
                else{
                    if (i==0 && j==0 )
                        dp[i][j] = {1, 1, 1};
                    else if (i == 0)
                        dp[i][j] = {dp[i][j-1][0]+1, 1, dp[i][j-1][2]+1};
                    else if (j == 0)
                        dp[i][j] = {1, dp[i-1][j][1]+1, dp[i-1][j][2]+1};
                    else{
                        dp[i][j][0] = dp[i][j-1][0]+1;
                        dp[i][j][1] = dp[i-1][j][1]+1;
                        dp[i][j][2] = cal_max_area(dp, i, j);
                        //update_ij_area(dp, i, j);
                    }
                }
                ans = max(ans, dp[i][j][2]);
            }
        return ans;
    }

    void update_ij_area(vector<vector<vector<int>>>& dp, int b_i, int b_j){
        int left_bound = dp[b_i][b_j][0];
        int row = dp[b_i][b_j][1];
        //在该列往上遍历找到每行1的最左边界；即每往上跳动一行计算一次矩形的面积，选最大的
        for(int count=0; count<row; count++){
            left_bound = min(left_bound, dp[b_i-count][b_j][0]);
            dp[b_i][b_j][2] = max(dp[b_i][b_j][2], left_bound*(count+1));
        }
    }

    int cal_max_area(vector<vector<vector<int>>>& dp, int b_i, int b_j){
        int left_bound = dp[b_i][b_j][0];
        int row = dp[b_i][b_j][1];
        int res = dp[b_i][b_j][2];
        //在该列往上遍历找到每行1的最左边界；即每往上跳动一行计算一次矩形的面积，选最大的
        for(int count=0; count<row; count++){
            left_bound = min(left_bound, dp[b_i-count][b_j][0]);
            res = max(res, left_bound*(count+1));
        }
        return res;
    }

};