//
// Created by LiHeng on 2020/6/21.
//

//最长公共子数组

#include <iostream>
#include <vector>

using namespace std ;
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size() ;
        int n = B.size() ;
        int longest = 0 ;
        vector<vector<int>> memo(m+1 ,vector<int> (n+1,0));
        for(int i=1 ; i < m+1 ; i++){
            for(int j = 1 ; j < n+1 ;j++){
                if(A[i-1] == B[j-1]){
                    memo[i][j] = memo[i-1][j-1] + 1 ;
                    longest = max(longest , memo[i][j]);
                }
                else
                    memo[i][j] = 0 ;
            }
        }
        return longest;
    }
};