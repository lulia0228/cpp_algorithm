

// 在排序数组中查找元素的第一个和最后一个位置  算法时间复杂度必须是 O(log n) 级别。
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2,-1);
        if (nums.size() == 0)
            return res;
        res[0] = find_first_target(nums, target);
        res[1] = find_last_target(nums, target);
        return res;
    }

    int find_first_target(vector<int>& nums, int target){
        int l=0, r=nums.size()-1, mid;
        while( l <= r){
            mid = l+(r-l)/2;
            if(nums[mid] < target)
                l = mid+1;
            else
                r = mid-1;
        }

        if(l<nums.size() && nums[l] == target)
            return l;

        return -1;
    }

    int find_last_target(vector<int>& nums, int target){
        int l=0, r=nums.size()-1, mid;
        while( l <= r){
            mid = l+(r-l)/2;
            if(nums[mid] > target)
                r = mid-1;
            else
                l = mid+1;
        }

        if(r >= 0 && nums[r] == target)
            return r;

        return -1;
    }

};