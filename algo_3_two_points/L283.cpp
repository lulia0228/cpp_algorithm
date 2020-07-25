//
// Created by LiHeng on 2020/4/23.
//

// 283 题目要求不能改变非0元素原来的顺序，而且要在原来数组上操作
#include <iostream>
#include <vector>
using namespace std;


class Solution{
public:
    void moveZeroes(vector<int>& nums){
        int k = 0;
        for (int i=0; i<nums.size();i++)
            if (nums[i])
                nums[k++] = nums[i];  //把非0元素移动到前面,后面补0
        for (int i=k; i<nums.size();i++)
            nums[i]=0;
    }

};

int main(){
    int arr[] = {1,0,1,0,3,12};
    vector<int> vec(arr, arr + sizeof(arr)/ sizeof(int));
    Solution().moveZeroes(vec);
    for (int i = 0 ; i < vec.size(); i++)
        cout<< vec[i]<<" ";
}



//下面的做法，不能保证非0元素顺序不变

class Solution1{
public:
    void moveZeroes(vector<int>& nums){
        int k = 0;
        for (int i=0; i<nums.size();i++)
            if (nums[i] && i!=k)
                swap(nums[k++] , nums[i]);  //0元素移动到前面
    }

};


//练习 leetcode   26 27 80

