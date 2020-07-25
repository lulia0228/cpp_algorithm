//
// Created by 李恒 on 2020/1/7.
//

//只出现一次的数字

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;
// 数学方法，利用异或位运算
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int i = 0; i < nums.size(); ++i){
            ans = ans^nums[i];
        }
        return ans;
    }
};

//哈希方法也可以，不过题目要求不得使用额外空间复杂度
class Solution1 {
public:
    // 使用哈希表
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> n;
        int ans = 0;
        for(int i = 0; i < nums.size(); ++i){
            n[nums[i]]++;
            // if(n.find(nums[i]) != n.end())
            //     n[nums[i]]++;
            // else
            //     n[nums[i]]=1;
        }
        unordered_map<int,int>::iterator iter;
        for(iter = n.begin();iter != n.end();iter++){
            if(iter->second == 1)
                ans = iter->first;
        }
        return ans;
    }
};

int main(){
    return 0;
}