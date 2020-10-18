

//最大正方形 注意和L85最大矩形区别

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int ans = 0;
        for (int i=0; i<m; ++i) {
            for (int j=0; j<n; ++j) {
                if (matrix[i][j] == '0') continue;
                // 受限于左上的 0, 受限于上边的 0, 受限于左边的 0
                // dp[i+1][j+1]代表以matrix[i][j]作为右下角的矩形的边长
                dp[i+1][j+1] = min(min(dp[i][j+1], dp[i+1][j]), dp[i][j]) + 1;
                ans = max(ans, dp[i+1][j+1]);
            }
        }
        return ans*ans;
    }
};
