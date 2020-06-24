//
// Created by LiHeng on 2020/6/21.
//

#include <iostream>
#include <vector>
using namespace std;

//动态规划思想提交后速度比较慢，贪心算法是最快的
//dp[1] 原来就有不需要操作 dp[1]=0
//dp[2] 复制1次A，再粘贴1次A 共2次操作 dp[2]=2

class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 2; i < n + 1; i++) {
            int minCount = i;//复制1次A+粘贴(i-1)次A
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    // i/j = [1次复制+（i/j-1)次粘贴操作]
                    minCount = min(dp[j] + i / j, minCount);
                }
            }
            dp[i] = minCount;
        }
        return dp[n];
    }
};


class Solution1 {
public:
    int minSteps(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 2; i < n + 1; i++) {
            int minCount = i;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    //minCount = min(dp[j] + i / j, minCount);
                    minCount = dp[j] + dp[i/j];
                    break;
                }
            }
            dp[i] = minCount;
        }
        return dp[n];
    }
};

//贪心算法  没看懂
#include <cmath>
class Solution2 {
public:
    int minSteps(int n) {
        if (n == 1) return 0;
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) return i + minSteps(n / i);
        }
        return n;
    }
};