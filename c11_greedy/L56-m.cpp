//
// Created by LiHeng on 2020/4/22.
//

//合并区间，按照区间起始值从小到大排序

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


//必须放在类外面或者放在里面要做成static
bool compare(const vector<int>& a , const vector<int>& b){
    return a[0] < b[0] ;
}

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        sort(intervals.begin(), intervals.end(), compare);
        for (int i=0 ; i<intervals.size(); ++i){
            if (res.empty() || intervals[i][0] > res[res.size()-1][1])
                res.push_back(intervals[i]);
            else
                res[res.size()-1][1] = max(intervals[i][1], res[res.size()-1][1]);
        }
        return res;
    }
};


//c++ 11以后 更便捷的写法
class Solution1 {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> ret;
        for (auto &i : intervals) {
            if (ret.empty() || i[0] > ret.back()[1]) ret.push_back(i);
            else ret.back()[1] = max(i[1], ret.back()[1]);
        }
        return ret;
    }
};