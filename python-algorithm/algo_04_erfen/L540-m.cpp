//
// Created by 李恒 on 2020/6/28.
//
#include <iostream>
#include <vector>

using namespace std ;
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int lt=0, rt=nums.size()-1, mid;
        while(lt < rt){
            mid = lt + (rt-lt)/2;
            if(mid%2 == 0){
                if(nums[mid] == nums[mid-1])
                    rt = mid-2;
                else
                    lt = mid;
            }
            else{
                if(nums[mid] == nums[mid-1])
                    lt = mid+1;
                else
                    rt = mid-1;
            }
        }
        return nums[lt];
    }
};