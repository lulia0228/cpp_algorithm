//
// Created by 李恒 on 2019/8/1.
//

//leetcode 219
//解决方法:滑动窗口+查找表

#include <iostream>
#include <unordered_set>
#include <vector>

using  namespace std;

class Solution{
public:
    bool containsNearbyDuplicate(vector<int>& nums , int k ){
        unordered_set<int> record;
        for(int i = 0 ; i < nums.size(); i++){
            if (record.find(nums[i]) != record.end())
                return true;
            record.insert(nums[i]);

            //始终保持查找表record中只有k个元素
            if(record.size() == k + 1)
                record.erase(nums[i - k]);  //删除record中最早插入的元素
        }
        return  false;
    }
};




