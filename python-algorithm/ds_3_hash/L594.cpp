
#include <iostream>
#include <map>
#include <vector>
using namespace std;
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int res = 0;
        //使用map 因为有有序的需求
        map<int,int> mp;
        for(auto n:nums)
            ++mp[n];
        for(auto p:mp){
            if(mp.find(p.first+1) != mp.end())
                res = max(res, p.second+mp[p.first+1]);
        }
        return res;
    }
};