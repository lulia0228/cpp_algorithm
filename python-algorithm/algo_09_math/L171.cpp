//
// Created by 李恒 on 2020/6/30.
//
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;
class Solution {
public:
    int titleToNumber(string s) {
        int n = s.size();
        int res = 0;
        for(int i=0; i<n; ++i)
            res += pow(26,n-1-i)*(s[i]-'A'+1);
        return res;
    }
};