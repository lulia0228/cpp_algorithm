
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int,int> m1;
        unordered_map<int,int> m2;
        unordered_map<int,int> m3;
        for(int i=0; i<nums.size(); ++i){
            ++m1[nums[i]];
            if(m2.find(nums[i]) == m2.end())
                m2[nums[i]] = i;
            m3[nums[i]] = i;
        }
        int degree = 1;
        int len = 1;
        for(auto p:m1){
            if(p.second>degree){
                degree = p.second;
                len = m3[p.first]-m2[p.first]+1;
            }
                //都是最大度的时候，找最短的，特殊分支
            else if (p.second == degree){
                len = min(len, m3[p.first]-m2[p.first]+1);
            }
        }
        return len;
    }
};

