
#include <iostream>
#include <vector>

using namespace std;
//这道题告诉我们，有时候要活用数组元素和它们的索引之间的关系
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int sz= arr.size();
        if (sz==0) return 0;
        int cursor = arr[0];
        int res = 0;
        for(int i=0; i<sz; ++i){
            cursor = max(cursor, arr[i]);
            if(cursor == i)
                ++res;
        }
        return res;
    }
};