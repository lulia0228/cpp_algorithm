//
// Created by LiHeng on 2020/6/27.
//

//set底层是红黑树 unordered_set 底层是哈希

//leetcode 220
#include <iostream>
#include <set>
#include <vector>


using namespace std;
class Solution{
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums , int k , int t ){

        set<long> record; //这里不用unordered_set是因为它的底层实现数据无序,需要利用set底层实现的有序性
        for(int i = 0 ; i < nums.size(); i++){
            //set.lower_bound()返回的是第一个满足要求的指针
            set<long>::iterator it = record.lower_bound((long)nums[i] - t);
            if (it != record.end() && *it <= (long)nums[i] + t)
                return true;
            record.insert(nums[i]);

            //始终保持查找表record中只有k个元素
            if(record.size() == k + 1)
                record.erase(nums[i - k]);  //删除record中最早插入的元素
        }
        return false;
    }
};

int main(){
    vector<int> v1 = {1,5,9,1,5,9};
    bool res = Solution().containsNearbyAlmostDuplicate(v1, 2, 3);
    cout << res;
}