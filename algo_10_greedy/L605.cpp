//
// Created by 李恒 on 2020/7/3.
//
//种花问题

#include <iostream>
#include <vector>

using namespace std;
// 一次遍历，同时看前后是否为0
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        int cnt = 0;
        for (int i = 0; i < len && cnt < n; i++) {
            if (flowerbed[i] == 1) {
                continue;
            }
            int pre = (i==0 ? 0:flowerbed[i-1]);
            int next = (i==len-1 ? 0:flowerbed[i+1]);
            if (pre==0 && next==0) {
                cnt++;
                flowerbed[i] = 1;
            }
        }
        return cnt >= n;
    }
};