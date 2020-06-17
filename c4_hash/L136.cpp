//
// Created by 李恒 on 2020/1/7.
//

//只出现一次的数字

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    // 使用哈希表
    int singleNumber1(vector<int>& nums) {
        unordered_map<int,int> n;
        int ans = 0;
        for(int i = 0; i < nums.size(); ++i){
            if(n.find(nums[i]) != n.end())
                n[nums[i]]++;
            else
                n[nums[i]]=1;
        }
        unordered_map<int,int>::iterator iter;
        for(iter = n.begin();iter != n.end();iter++){
            if(iter->second == 1)
                ans = iter->first;
        }
        return ans;
    }

    // 数学方法，利用异或位运算
    int singleNumber2(vector<int>& nums) {
        int ans = 0;
        for(int i = 0; i < nums.size(); ++i){
            ans = ans^nums[i];
        }
        return ans;
    }

};











int main(){

    return 0;
}