

#include <iostream>
#include <cassert>
#include <vector>

using namespace std ;

class Solution{
public:

    //leetcode 704 二分查找 是否存在
    int search(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size() -1 ;
        while(i <= j){
            int middle = i + (j - i)/2 ;
            if(nums[middle] == target)
                return middle ;
            else if (nums[middle] > target)
                j = middle - 1 ;
            else
                i = middle + 1 ;
        }
        return -1 ;
    }
    
};


