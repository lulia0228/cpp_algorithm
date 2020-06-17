//
// Created by LiHeng on 2020/5/23.
//
//这道题两种方法，暴力解法就不说了，一种是优先级队列，另一种是二分法

//这里的二分法，二分的不是索引，而是实际值，通过判断矩阵中<=mid的元素多少，来确定值的区间。
//最核心的是，在判断矩阵中<=mid的元素个数时候，采用从左下角或者右上角搜索的特殊方式，充分利用题目元素排布顺序特性,路径最长是从左下角到右上角即（2n-1)
//时间复杂度为2nlog(max-min)。空间复杂度为O(1)。
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int row = matrix.size();
        int col = matrix[0].size();
        int left = matrix[0][0];
        int right = matrix[row-1][col-1];
        while(left < right){
            int mid = left + (right-left)/2;
            //找二维矩阵中，值小于等于mid的个数
            int count = findNotBiggerThanMid(matrix, mid, row , col);
            if (count<k)
                left = mid+1;
            else
                right = mid;
        }
        //return right;
        return left;

    }

    int findNotBiggerThanMid(vector<vector<int>>& matrix, int mid, int row, int col){
        //从左下角搜索，找小于等于mid；如果从右上角找就是找大于等于mid
        int i = row-1;
        int j = 0;
        int count = 0;
        while(i>=0 && j<col){
            if(matrix[i][j]<=mid){
                count += i+1; //当前元素所在列的上方的元素全部都小于mid
                j++;
            }
            else
                i--;
        }
        return count;
    }
};


//优先级队列  时间复杂度n*nlogk
#include <queue>
class Solution1 {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int, vector<int>, less<>> q;
        for(auto vec:matrix)
            for(auto x:vec){
                if(q.size() == k){
                    if(x<=q.top()){
                        q.pop();
                        q.push(x);
                    }
                }
                else
                    q.push(x);
            }
        return q.top();
    }
};



