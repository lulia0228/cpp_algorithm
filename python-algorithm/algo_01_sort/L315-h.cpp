//
// Created by 李恒 on 2020/7/2.
//

// Leetcode 315 比较难的一道题：计算右侧小于当前元素的个数 用到了归并排序的逆序度概念 返回每个元素位置右侧小于它的个数
// 剑指offer 51 求数组中的逆序对（暴力法双层遍历 + 归并排序）

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> res;

    vector<int> countSmaller(vector<int>& vec) {
        if (vec.empty())
            return {};
        vector<pair<int, int>> nums;
        for (int i = 0; i < vec.size(); i++)
            //nums.emplace_back(vec[i], i); //两种写法都可以，c++ 11后加的用法，插入效率更高
            nums.push_back(make_pair(vec[i], i));
        res = vector<int>(vec.size(), 0);
        merge_sort(nums, 0, nums.size() - 1);
        return res;
    }

    void merge_sort(vector<pair<int, int>>& nums, int left, int right){
        if (left < right){
            int mid = left + (right - left) / 2;
            merge_sort(nums, left, mid);
            merge_sort(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }

    void merge(vector<pair<int, int>>& nums, int left, int mid, int right){
        int i = left, j = mid + 1;

        vector<pair<int, int>> sort_nums;

        while (i <= mid && j <= right){
            if (nums[i].first <= nums[j].first){
                res[nums[i].second] += j - mid - 1; //左边序列元素出列的时候计算下右边序列已经出列的个数
                sort_nums.push_back(nums[i++]);
            }else if (nums[i].first > nums[j].first){
                sort_nums.push_back(nums[j++]);
            }
        }

        while (i <= mid){
            res[nums[i].second] += j - mid - 1;  //左边序列元素出列的时候计算下右边序列已经出列的个数
            sort_nums.push_back(nums[i++]);
        }

        while (j <= right){
            sort_nums.push_back(nums[j++]);
        }

        for (int m = 0, n = left; m < sort_nums.size(); m++, n++){
            nums[n] = sort_nums[m]; //每次小合并后在原数组上相应位置赋值
        }
    }
};