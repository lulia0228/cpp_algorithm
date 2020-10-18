

//leetcode 350
//查找问题 类型2 map解决 map可以理解为字典
#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2){

        map<int, int> record; //键存放元素,值存放频次
        for(int i = 0 ; i < nums1.size() ; i++)
            if (record.find(nums1[i]) == record.end()) //如果map中不存在键
                record.insert(make_pair(nums1[i] , 1));
            else
                record[nums1[i]] ++ ; //如果键已经存在

        vector<int> resultVector;
        for(int i = 0 ; i < nums2.size() ; i++)
            if(record.find(nums2[i]) != record.end() && record[nums2[i]] > 0){
                resultVector.push_back(nums2[i]);
                record[nums2[i]] --;
                if (record[nums2[i]] == 0) //元素频次为0,删除键
                    record.erase(nums2[i]);
            }

        return resultVector;
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




