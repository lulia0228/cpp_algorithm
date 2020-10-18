
#include <iostream>
#include <vector>

using namespace std ;
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int sz = A.size();
        if(sz < 3) return 0;
        //dp[i]表示以A[i]作为结尾的等差子序列的个数
        vector<int> dp(sz, 0);
        for(int i=2; i<sz; ++i){
            if(A[i]-A[i-1] == A[i-1]-A[i-2])
                dp[i] = dp[i-1]+1;
        }
        int total=0;
        for(auto n:dp)
            total += n;
        return total;
    }
};