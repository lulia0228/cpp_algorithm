//
// Created by 李恒 on 2019/8/1.
//


//two sum 问题 和前面出现的区别在于:给的不是有序数组.

// 将元素放入查找表, 对于元素a, 在查找表中查找target-a
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cassert>

using namespace std;

//为了避免相等的两个元素互相覆盖的问题,在遍历第a个元素的时候,只把其前面的元素放入查找表

class Solution{
public:
    vector<vector<int>> twoSum(vector<int>& nums , int target){
        unordered_map<int , int> record;
        vector<vector<int>> resultVec;

        for(int i = 0 ; i < nums.size() ; i++){

            int comple = target - nums[i];
            if (record.find(comple) != record.end()){
                int res[2] = {i , record[comple]};
                resultVec.push_back( vector<int> (res, res + 2 ) );  //vector 用push_back 不是insert
            }

            record[nums[i]] = i; //键存储元素,值存储索引 这里遍历处理完第a个元素后才把其索引放进去
        }

        cout << "Numbers of solution : " << resultVec.size()<< endl;

        if (resultVec.size() == 0)
            throw  invalid_argument(" The input has no solution .");     //放在函数内部

        return  resultVec;
    }
};


// 两数之和 L2
// 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

// 注意这个题目先不要想着用双指针对撞，因为双指针对撞需要先排序，如此一来下标就丢失了

//两种方法 1 ：遍历数组，遍历当前元素nums[i]，再遍历其后的所有元素寻找与target-nums[i]相等的值，这样时间复杂度是O（n*n)
//         2 ：借助哈希表，把每个元素的下标作为值存储，依然遍历nums[i]在哈希表中查找target-nums[i]，时间复杂度是O（n）

//   扩充：如果这道题目，没有前提假设只有一个对应答案的话（可能会出现多组答案和重复值两种情况），方法2需要做部分修改
// （即哈希表存储的时候把相同的值的不同下标当做VALUE存储到一个vector中后续再做处理），


//map底层是红黑树（可当做有序的字典使用）   unordered_map底层是哈希表

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um1;
        vector<int> vec;
        for(int i=0; i<nums.size(); i++)
            um1.insert(pair<int,int>(nums[i],i));
        for(int i=0; i<nums.size(); i++){
            if (um1.find(target - nums[i]) != um1.end()) {
                if (um1[target - nums[i]] != i ){ //这是因为可能元素本身被用了2次，如3+3=6;这里改写成下面做法的更高级
                    vec.push_back(i);
                    vec.push_back(um1[target - nums[i]]);
                    break;
                }
            }
        }
        return vec;
    }
};

//这样写速度更快
class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um1;
        vector<int> vec;
        for(int i=0; i<nums.size(); i++){
            if (um1.find(target - nums[i]) != um1.end()) {
                vec.push_back(i);
                vec.push_back(um1[target - nums[i]]);
                break;
            }
            else
                um1[nums[i]] = i;
        }
        return vec;
    }
};

int main(){
    int arr[] = {2,1,7,0,4,1,5,14,21,6,12,3};
    vector<int> vec1(arr, arr + sizeof(arr)/ sizeof(int));
    vector<vector<int>> re = Solution().twoSum(vec1, 9);
//    cout<< re.size() << endl;
    for (int i = 0 ; i < re.size() ; i++){
        if (i != 0)
            cout << endl;
        for (int j = 0 ; j < re[i].size() ; j++)
            cout << re[i][j]<< " ";
    }
}


//注意上面这么做 如果有多种解 可以全部返回

//练习题 leetcode 15 18 16

