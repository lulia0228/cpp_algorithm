//
// Created by LiHeng on 2020/4/23.
//

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for(int i=0; i<nums.size(); ++i){
            if(nums[i] != (i+1)){
                while(nums[i] != nums[nums[i]-1])
                    swap(nums[i], nums[nums[i]-1]);
            }
        }
        vector<int> res;
        for(int i=0; i<nums.size(); ++i)
            if(nums[i] != (i+1))
                res.push_back(i+1);
        return res;
    }
};

// 方法2 如果某个索引对应的是消失的数字，那么如果把其它索引对应的值作为索引处理，最后一定处理不到消失的数字对应的索引。
// 所以思路：怎么处理没消失的数字对应的索引，使得消失的数字对应的索引上的值体现特殊性？？？
// 答案是把没消失的数字对应的索引上的值全部加上数组长度n，这样以来消失的数字对应的索引上的值绝对是小于等于n的。

class Solution1 {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int sz = nums.size();
        for(int i=0; i<nums.size(); ++i){
            //int index= (nums[i]-1)%nums.size(); //不知道为什么在leetcode页面上不取余会报错
            //nums[index] += sz;
            nums[nums[i]-1] += sz;
        }
        vector<int> res;
        for(int i=0; i<nums.size(); ++i)
            if(nums[i] <= sz)
                res.push_back(i+1);
        return res;
    }
};

int main(){
    vector<int> v1{4,3,2,7,8,2,3,1};
    vector<int> re = Solution().findDisappearedNumbers(v1);
    for(auto i:re)
        cout << i << endl;
}