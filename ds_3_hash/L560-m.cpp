
//和为K的连续子数组

// 这个题目 我一开始想用动态规划 动态规划貌似做不了啊

/*遍历数组nums，计算从第0个元素到当前元素的和，用哈希表保存出现过的累积和sum的次数。
如果sum - k在哈希表中出现过，则代表从当前下标i往前有连续的子数组的和为sum。
时间复杂度为O(n)，空间复杂度为O(n)O(n)。*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int subarraySum(vector<int> &nums, int k) {
        int sum = 0, res = 0;
        unordered_map<int, int> cul;
        cul[0] = 1;
        //存下来所有累计和的哈希计数
        for (auto m : nums) {
            sum += m;
            res += cul[sum - k];
            ++cul[sum];
        }
        return res;
    }
};

//如果需要返回连续子数组，可以在map中存储每个sum对应的索引


//方法二暴力法
//使用两层循环，计算2个索引之间的累计和

class Solution1 {
public:
    int subarraySum(vector<int> &nums, int k) {
        int size = nums.size(), res = 0;
        for (int i = 0; i < size; ++i) {
            int sum = 0;
            for (int j = i; j < size; ++j) {
                sum += nums[j];
                res += sum == k ? 1 : 0;
            }
        }
        return res;
    }
};

