//
// Created by LiHeng on 2020/6/30.
//
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<1)
            return false;
        while(n%3 == 0)
            n = n/3;
        return n==1;
    }
};