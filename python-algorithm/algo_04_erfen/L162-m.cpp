//
// Created by 李恒 on 2020/6/28.
//
#include <iostream>
#include <cassert>
#include <vector>

using namespace std ;
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int lt = 0 , rt = nums.size()-1;
        while(lt < rt){
            int mid = lt+(rt-lt)/2;
            if(nums[mid] > nums[mid+1]) //中点是降序，说明峰值在左边，因此更新右边界
                rt = mid;
            else
                lt = mid+1;
        }
        return lt; //最终lt rt一样
    }
};

// 这道题题目设置特殊，且只需要返回一个峰值，所以用二分法可以
// 另外一种方法就是一趟遍历时间复杂度不符合要求，代码如下：


class Solution1 {
public:
    int findPeakElement(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++)
            if (nums[i] > nums[i + 1])
                return i;
        return nums.size() - 1;
    }
};