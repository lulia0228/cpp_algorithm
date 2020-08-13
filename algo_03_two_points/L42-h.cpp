//
// Created by 李恒 on 2020/8/13.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int sz = height.size();
        if(sz <= 2) return 0;
        int res = 0;
        int left = 0, right = sz-1;
        int l_max = height[0], r_max = height[sz-1];
        while(left <= right){
            l_max = max(l_max, height[left]);
            r_max = max(r_max, height[right]);
            if(l_max <= r_max){
                res += l_max - height[left];
                ++left;
            }
            else{
                res += r_max - height[right];
                --right;
            }
        }
        return res;
    }
};