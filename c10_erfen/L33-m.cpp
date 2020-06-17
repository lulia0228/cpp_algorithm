//
// Created by LiHeng on 2020/4/21.
//

//搜索旋转数组   算法时间复杂度必须是 O(log n) 级别。

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0 ,right = nums.size() - 1, mid;
        while(left <= right){
            mid = left + (right-left)/2;
            if(nums[0] > target){  //目标在右子数组
                if(nums[mid] >= nums[0]) left = mid + 1; //中点在左子数组
                else{ //中点在右子数组
                    if(nums[mid] == target) return mid;
                    else if(nums[mid] < target) left = mid + 1;
                    else right = mid - 1;
                }
            }
            else {//目标在左子数组
                if(nums[mid] < nums[0]) right = mid-1;//中点在右子数组
                else{ //中点在左子数组
                    if(nums[mid] == target) return mid;
                    else if(nums[mid] < target) left = mid+1;
                    else right = mid-1;
                }
            }
        }
        return -1;
    }
};