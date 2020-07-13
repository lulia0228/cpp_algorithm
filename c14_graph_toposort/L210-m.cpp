//
// Created by LiHeng on 2020/7/12.
//

#include <iostream>
#include <vector>
using  namespace std;
class Solution {
public:
    vector<int> res;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> flag(numCourses, 0);
        vector<vector<int>> adjacency(numCourses, vector<int>());
        for(auto vec: prerequisites)
            //adjacency[vec[1]].push_back(vec[0]);
            adjacency[vec[1]].push_back(vec[0]);
        for(int i=0; i<numCourses; ++i)
            if (!dfs(i, flag, adjacency))
                return vector<int>();
        reverse(res.begin(), res.end()); //为什么要反序，思考下
        return res;
    }

    bool dfs(int index, vector<int>& flag, vector<vector<int>>& adjacency){
        if(flag[index] == -1) return true;
        if(flag[index] == 1) return false;
        flag[index] = 1;
        for(auto j:adjacency[index]) //注意adjacency[index]里面存放的是index节点的所有邻接节点
            if (!dfs(j, flag, adjacency))
                return false;
        flag[index] = -1;
        res.push_back(index);
        return true;
    }
};