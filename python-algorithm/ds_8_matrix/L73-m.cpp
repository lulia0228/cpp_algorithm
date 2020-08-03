//
// Created by 李恒 on 2020/7/1.
//
#include <iostream>
#include <vector>
using namespace std;

//不使用额外空间
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        //先标记处第一列是否有0
        int col_0 = matrix[0][0];
        for(int i=0; i<matrix.size(); ++i)
            if(matrix[i][0] == 0){
                col_0 = 0;
                break;
            }
        //用每行第一个数字标记该行是否有0
        for(int i=0; i<matrix.size(); ++i)
            for(int j=0; j<matrix[0].size(); ++j)
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    break;
                }
        //从第二列开始，用各列第一个数字标记该列是否有0
        for(int j=1; j<matrix[0].size(); ++j)
            for(int i=0; i<matrix.size(); ++i)
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    break;
                }
        //先不处理第一行 第一列 会对别的列产生干扰
        for(int i=1; i<matrix.size(); ++i)
            for(int j=1; j<matrix[0].size(); ++j){
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] =0;
            }

        //现在处理第一行
        if(matrix[0][0] == 0)
            for(int i=1; i<matrix[0].size(); ++i)
                matrix[0][i] = 0;

        //现在处理第一列
        if(col_0 == 0)
            for(int i=0; i<matrix.size(); ++i)
                matrix[i][0] = 0;


    }
};

//使用额外空间复杂度
#include <unordered_set>
class Solution1 {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        //MxN矩陣
        int m=matrix.size(),n=matrix[0].size();
        unordered_set<int> bm,bn;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if(matrix[i][j]==0){
                    bm.insert(i);
                    bn.insert(j);
                }
            }
        }
        for(auto row:bm){
            for( int x = 0; x < n; x++)
                matrix[row][x] = 0;
        }
        for(auto col:bn){
            for( int x = 0; x < m; x++)
                matrix[x][col] = 0;
        }

    }
};