//
// Created by 李恒 on 2020/7/1.
//
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0)
            return false;
        int r = 0;
        int c = matrix[0].size()-1;
        while(r < matrix.size() && c >= 0){
            if (target < matrix[r][c])
                c--;
            else if(target > matrix[r][c])
                r++;
            else
                return true;
        }
        return false;
    }
};