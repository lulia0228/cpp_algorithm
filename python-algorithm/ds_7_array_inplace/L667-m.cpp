//
// Created by 李恒 on 2020/6/29.
//
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ret(n,0) ;
        ret[0] = 1;
        for (int i=1, interval=k; i<=k; i++, interval--) {
            ret[i] = i%2 == 1 ? ret[i-1] + interval : ret[i-1] - interval;
        }
        for (int i = k + 1; i < n; i++) {
            ret[i] = i + 1;
        }
        return ret;
    }
};