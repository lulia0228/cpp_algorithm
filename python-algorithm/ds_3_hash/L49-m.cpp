

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <unordered_map>
using namespace std;


//借助一个无序字典实现；时间复杂度 k*n*logn 其中n是字符串长度 k是字符串个数
//空间复杂度k*n
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> um1;
        for(int i=0; i<strs.size(); i++){
            string tmp_str = strs[i];
            sort(tmp_str.begin(), tmp_str.end());
            um1[tmp_str].push_back(strs[i]);
        }
        for(auto x:um1)
            res.push_back(x.second);
        return res;
    }
};

//还有一个办法是遍历一趟字符串，记下每个字符出现的个数，然后将其转化成一个key（这个key可以是26个字母个数组成向量）,这个key当做无序字典的key
//这样相当于不再做排序，时间复杂度变成线性，就是key变长了