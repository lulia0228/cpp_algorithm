
// 三数之和
//写的时候遇到困难
//解题思路：排序后，顺序遍历每个元素，在当前元素后方选2个元素用双指针夹逼，注意去重就好了

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res_final;
        sort(nums.begin(), nums.end());
        if (nums.size() < 3 || nums[0] > 0 || nums[nums.size()-1] < 0)
            return res_final;

        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i-1])//跳过相同的数字
                continue;
            int k = i + 1;
            int m = nums.size() - 1;

            while(k < m) {
                int s = nums[i] + nums[k] + nums[m];
                if (s < 0) {
                    ++k;
                }
                else if (s > 0) {
                    --m;
                }
                else {
                    vector<int> res;
                    res.push_back(nums[i]);
                    res.push_back(nums[k]);
                    res.push_back(nums[m]);
                    res_final.push_back(res);
                    while(k<m && nums[k]==nums[k+1]) ++k;
                    while(k<m && nums[m]==nums[m-1]) --m;
                    ++k;
                    --m;
                }
            }
        }
        return res_final;
    }
};

//耗时最短
class Solution1 {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()<3) return res;
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size(); i++){
            if(nums[i]>0)  break;
            if(i>0 && nums[i]==nums[i-1])  continue;
            int l = i+1;
            int r = nums.size()-1;
            while(l < r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum == 0){
                    int tmp[] = {nums[i], nums[l], nums[r]};
                    res.push_back(vector<int>(tmp, tmp+3));
                    while(l<r && nums[l]==nums[l+1]) l++;
                    while(l<r && nums[r]==nums[r-1]) r--;
                    l++;
                    r--;
                }
                else if(sum < 0) l++;
                else if(sum > 0) r--;
            }
        }
        return res;
    }
};

