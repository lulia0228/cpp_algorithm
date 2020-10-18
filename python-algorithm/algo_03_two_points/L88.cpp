
//88 合并两个有序数组

//思路比较独特，倒着处理数组

//此题输入中设定数组1后面存在足够空间存放合并后的数据;要求不开辟多余的内存完成合并


//输入:
//nums1 = [1,2,3,0,0,0], m = 3
//nums2 = [2,5,6],       n = 3


#include <iostream>
#include <vector>
using namespace std;

class Solution {

public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n-1;
        while(i >= 0 && j >= 0){
            if(nums1[i] > nums2[j]){
                nums1[k--] = nums1[i];
                --i;
            }
            else{
                nums1[k--]=nums2[j];
                --j;
            }
        }
        while(j>=0)
            nums1[k--] = nums2[j--];
    }

    //合并2个有序数组到一个新的数组中
    vector<int> mergeTwoArrayList(vector<int>& nums1, int m , vector<int>& nums2 , int n ){
        vector<int> res ;
        int i = 0 , j = 0 ;
        while(i < m && j < n){
            if(nums1[i] > nums2[j]){
                res.push_back(nums2[j]);
                j++ ;
            }
            else {
                res.push_back(nums1[i]);
                i++ ;
            }
        }

        while(i < m){
            res.push_back(nums1[i]);
            i++ ;
        }

        while(j < n){
            res.push_back(nums2[j]);
            j++ ;
        }

        return res ;
    }

};