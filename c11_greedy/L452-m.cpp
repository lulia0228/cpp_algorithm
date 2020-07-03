//
// Created by 李恒 on 2020/7/3.
//

//也是计算不重叠的区间个数，不过和 Non-overlapping Intervals 的区别在于，[1, 2] 和 [2, 3] 在本题中算是重叠区间。

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int sz=points.size();
        if(sz == 0) return 0;
        sort(points.begin(), points.end(), cmp);
        int count=1;
        int end = points[0][1];
        for(int i=1; i<sz; ++i){
            if(points[i][0]<=end)
                continue;
            ++count;
            end = points[i][1];
        }
        return count;
    }

    static bool cmp(vector<int>&a, vector<int>&b){
        return a[1] < b[1]; //从小到大排
    }
};