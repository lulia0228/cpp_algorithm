


//按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间。

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int sz=intervals.size();
        if(sz == 0) return 0;
        sort(intervals.begin(), intervals.end(), cmp);
        int count=1;
        int end = intervals[0][1];
        for(int i=1; i<sz; ++i){
            if(intervals[i][0]<end)
                continue;
            ++count;
            end = intervals[i][1];
        }
        return sz-count;
    }

    static bool cmp(vector<int>&a, vector<int>&b){
        return a[1] < b[1]; //从小到大排
    }
};