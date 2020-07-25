//
// Created by LiHeng on 2020/6/3.
//
#include <iostream>
#include <cmath>
using namespace std;
class Solution {
public:
    bool judgeSquareSum(int c) {
        int i = 0;
        int j = (int)sqrt(c);
        while(i<=j){
            int sum = -c + i*i + j*j; //一开始使用的是i*i+j*j 太大的数字会报错，然后用i*i+j*j-c还是报错，最后用-c+i*i+j*j
            if(sum == 0)
                return true;
            else if (sum < 0)
                ++i;
            else
                --j;
        }
        return false;
    }
};