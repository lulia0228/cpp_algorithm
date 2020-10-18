

// 这道题由153演化而来，区别就是有重复元素
// 下面的解法和153的改动在于： else if 分支
// 处理的是旋转数组是从重复数字中的某一位置断开的特殊情况 如 2 0 1 2 2  或者 2 2 0 1 2
// 处理的方法就是把 后面数组的末尾给删除掉，形成一个新的数组，然后按照153的方法处理新的数组


// 2 2 2 0 1 这种情况无需特殊考虑 153的解法就可以处理

#include <iostream>
#include <cassert>
#include <vector>

using namespace std ;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int sz = nums.size();
        int lt=0, rt=sz-1, mid;
        if(nums[0] < nums[sz-1])
            return nums[0];
        else if (nums[0] == nums[sz-1]){
            while(rt>0 && nums[rt] == nums[sz-1])
                --rt;
            if(nums[0] < nums[rt])
                return nums[0];
            while(lt < rt){
                mid = lt + (rt-lt)/2;
                if(nums[mid] >= nums[0]) //这里比较mid与left是行不通的,原因我也没明白
                    lt = mid+1;
                else
                    rt = mid;
            }
        }
        else{
            while(lt < rt){
                mid = lt + (rt-lt)/2;
                if(nums[mid] >= nums[0]) //这里比较mid与left是行不通的
                    lt = mid+1;
                else
                    rt = mid;
            }
        }
        return nums[lt];
    }
};

class Solution1 {
public:
    int findMin(vector<int>& nums) {
        int sz = nums.size();
        int lt=0, rt=sz-1, mid;
        if(nums[0] < nums[rt])
            return nums[0];
        else if (nums[0] == nums[sz-1]){
            while(rt>0 && nums[rt] == nums[sz-1])
                --rt;
            if(nums[0] < nums[rt])
                return nums[0];
            while(lt < rt){
                mid = lt + (rt-lt)/2;
                if(nums[mid] <= nums[rt])
                    rt = mid;
                else
                    lt = mid+1;
            }
        }
        else{
            while(lt < rt){
                mid = lt + (rt-lt)/2;
                if(nums[mid] <= nums[rt])
                    rt = mid;
                else
                    lt = mid+1;
            }
        }
        return nums[lt];
    }
};
