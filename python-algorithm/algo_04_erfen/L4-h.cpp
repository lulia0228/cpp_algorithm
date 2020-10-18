
//L4
#include <iostream>
#include <vector>
using namespace std ;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        //小trick：无论(m+n)是奇数还是偶数，(m+n+1)/2和(m+n+2)/2两个下标对应的值取平均后都是我们想要的中位数。
        int l1 = nums1.size() , l2 = nums2.size() , left_all = (l1+l2+1)/2 , right_all = (l1+l2+2)/2 ;
        if(nums1.size() == 0)
            return (nums2[(l2+1)/2] + nums2[(l2+2)/2])/2 ;
        if(nums2.size() == 0)
            return (nums1[(l1+1)/2] + nums1[(l1+2)/2])/2 ;

        return (findKth(nums1,0,nums2,0,left_all)+findKth(nums1,0,nums2,0,right_all))/2 ;
    }

    //函数：寻找两个数组的第K位数
    double findKth(vector<int>& nums1, int nums1_start, vector<int>& nums2, int nums2_start, int k){
        //判断起始索引是否越界
        if(nums1_start>=nums1.size())
            return nums2[nums2_start + k - 1];
        if(nums2_start>=nums2.size())
            return nums2[nums1_start + k - 1];
        //K=1，表示我们要找第一个元素，只要比较两个数组的第一个元素，返回较小的那个
        if(k == 1)
            return min(nums1[nums1_start],nums2[nums2_start]);
        //
        int midValue1 = (nums1_start + k/2 - 1 < nums1.size()) ? nums1[nums1_start + k/2 - 1] : INT_MAX;
        int midValue2 = (nums2_start + k/2 - 1 < nums1.size()) ? nums2[nums2_start + k/2 - 1] : INT_MAX;
        //更新2个数组的起始位置；谁小就把谁的起始搜索位置更新到它的下一位
        if(midValue1 < midValue2)
            return findKth(nums1, nums1_start + k/2, nums2, nums2_start, k - k/2);
        else
            return findKth(nums1, nums1_start, nums2, nums2_start + k/2, k - k/2);
    }
};