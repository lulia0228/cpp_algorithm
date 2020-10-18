

//c++中map set  底层实现为平衡二叉树  插入 查找 删除 时间复杂度都是logn
//c++中也提供了 unordered_map unordered-set底层实现为哈希表 之所以叫unordered是因为哈希表丧失了顺序性

//
// Created by 李恒 on 2019/8/1.
//

//leetcode 349
//查找问题 类型1 set解决
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2){
        // o(n)    如果使用set是 o(nlogn)
        unordered_set<int> record(nums1.begin(), nums1.end()); // 替代前面的循环

        unordered_set<int> resultSet;
        for(int i = 0 ; i < nums2.size() ; i++)
            if(record.find(nums2[i]) != record.end())
                resultSet.insert(nums2[i]);

        return vector<int> (resultSet.begin() , resultSet.end()); // 替代上面的循环
    }
};

class Solution1{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2){
        set<int> record;
        for(int i = 0 ; i < nums1.size() ; i++)
            record.insert(nums1[i]);

//        set<int> record(nums1.begin(), nums1.end()); // 替代前面的循环

        set<int> resultSet;
        for(int i = 0 ; i < nums2.size() ; i++)
            if(record.find(nums2[i]) != record.end())
                resultSet.insert(nums2[i]);

//        vector<int> resultVector;
//        for(set<int>::iterator iter = resultSet.begin() ; iter != resultSet.end() ; iter++ )
//            resultVector.push_back(*iter);
//        return resultVector;

        return vector<int> (resultSet.begin() , resultSet.end()); // 替代上面的循环
    }
};
int main(){
    int arr1[] = {1,2,2,1};
    int arr2[] = {2,3,3,2};
    vector<int> vec1(arr1, arr1 + sizeof(arr1)/ sizeof(int));
    vector<int> vec2(arr2, arr2 + sizeof(arr2)/ sizeof(int));
    vector<int> re = Solution().intersection(vec1 , vec2);
    for (int i =0 ; i < re.size() ; i++)
        cout << re[i] << " ";
}

//练习 leetcode 242 202 290 205 451  用c++的查找表解决




