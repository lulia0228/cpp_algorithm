//
// Created by LiHeng on 2020/6/28.
//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//方法1 反转3次 2*O(N)

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k % nums.size());
        reverse(nums.begin() + k % nums.size(), nums.end());
    }
};

//方法2 环状替换 这个一直不懂

class Solution1 {
public:
    void rotate(vector<int>& nums, int k) {
        int len  = nums.size();
        k = k % len;
        int count=0;
        for(int start = 0; count < len; start++) {
            int cur = start;
            int pre = nums[cur];
            do{
                int next = (cur + k%len) % len;
                int temp = nums[next];    // 先标记下来
                nums[next] = pre;
                pre = temp;
                cur = next;
                count++;
            }while(cur != start)  ;     // 循环暂停，回到起始位置

        }
    }
};
