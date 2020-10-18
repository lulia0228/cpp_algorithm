

//删除排序数组中的重复项
//要求不借助额外的空间；找出不重复的元素个数k，并且按顺序放在数组前k个位置，原数组第k个元素后面的元素不用管。


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int flag = nums[0];
        int index = 0;
        for(int i=0 ; i<nums.size() ; i++){
            if(nums[i] != flag){
                index++ ;
                nums[index] = nums[i];
                flag = nums[i];
            }
        }
        return index+1;
    }
};