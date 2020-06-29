//
// Created by 李恒 on 2020/6/29.
//
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n= matrix[0].size();
        vector<vector<int>> record(m+n-1, vector<int>());
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                record[i-j+n-1].push_back(matrix[i][j]);
            }
        }
        for(int i=0; i<record.size(); ++i){
            if (!IsAllEqual(record[i]))
                return false;
        }
        return true;
    }

    bool IsAllEqual(vector<int> &num){
        for(int i=1; i<num.size(); ++i){
            if(num[i] != num[i-1])
                return false;
        }
        return true;
    }
};


// 3行4列 副对角线行列索引差值
// 2 1 0 -1 -2 -3

//更快
class Solution1 {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n= matrix[0].size();
        for(int i=1; i<m; ++i){
            for(int j=1; j<n; ++j){
                if(matrix[i][j] != matrix[i-1][j-1] )
                    return false;
            }
        }
        return true;
    }

};