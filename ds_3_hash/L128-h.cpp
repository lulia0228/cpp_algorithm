//
// Created by LiHeng on 2020/4/23

//C++ 11中出现了两种新的关联容器:unordered_set和unordered_map，其内部实现与set和map大有不同，
//set和map内部实现是基于RB-Tree，而unordered_set和unordered_map内部实现是基于哈希表(hashtable)


//题目;给定一个未排序的整数数组，找出最长连续序列的长度。
//要求算法的时间复杂度为 O(n)。

// 思路就是先把所有数放到哈希表中，遍历原始数组，找到每个数 左右两边能到达的最大长度，遍历一个数，
// 就可以把其相邻的数全部在哈希表中删除， 防止重复遍历;
// 值得注意这个删除操作并不会影响最长值的计算，反而会加速，这点要想明白！！！

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();
        unordered_set<int> hashSet;
        for (int i = 0; i < nums.size(); i++)
            hashSet.insert(nums[i]);

        int maxConSeqLen = 0;
        for (int i = 0; i < nums.size(); i++) {
            //erase的使用很巧妙。哈希表中存在该key则删除 且返回1；否则直接返回0 可以省去find操作
            if (hashSet.erase(nums[i])) {
                int num = nums[i];
                int curLen = 1;
                //往右找
                while (hashSet.erase(++num))
                    curLen++;
                //往左找
                num = nums[i];		//该步骤是因为num发生了改变 必须变回nums[i]
                while (hashSet.erase(--num))
                    curLen++;
                maxConSeqLen = (maxConSeqLen > curLen ? maxConSeqLen : curLen);
            }
        }
        return maxConSeqLen;
    }
};

// 下面这思路也可以。
// 思想：最长连续序列的最小值一定是数组中的某个值，那遍历的时候只用分析以这个最小值开头的连续序列就可以了。
// 怎么判断一个元素是不是连续序列的开头呢，看下面代码。
class Solution1 {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        unordered_set<int> myset(nums.begin(), nums.end());
        int res = 0;
        for(auto num : nums){
            if(myset.count(num-1) == 0){
                int next = num + 1;
                while(myset.count(next))
                    next ++;
                res = max(res, next-num);
            }
        }
        return res;
    }
};

