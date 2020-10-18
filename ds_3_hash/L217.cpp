

//存在重复元素

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> mp1;
        for(int i=0;i<nums.size();++i){
            mp1[nums[i]]++;
            if(mp1[nums[i]] >=2)
                return true;
        }
        return false;
    }
};

class Solution1 {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> mp1;
        for(int i=0;i<nums.size();++i){
            if(mp1.find(nums[i]) != mp1.end()){
                return true;
            }
            else
                mp1[nums[i]] = 1;
        }
        return false;
    }
};

int main(){
    return 0 ;
}