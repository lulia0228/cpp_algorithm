//
// Created by LiHeng on 2020/4/22.
//
#include <iostream>
#include <vector>
using namespace std;


//先转置；再前后对称互换列
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int i=0 ; i<matrix.size(); ++i){
            for (int j=i+1; j<matrix[0].size(); ++j)
                swap(matrix[i][j],matrix[j][i]); //一开始犯了个巨大错误，c++中某个元素应该是matrix[i][j] ，不是matrix[i，j]
        }
        for(int i=0 ; i<matrix.size(); ++i){
            for (int j=0; j<matrix[0].size()/2; ++j)
                swap(matrix[i][j],matrix[i][matrix[0].size()-j-1]);
        }
    }
};