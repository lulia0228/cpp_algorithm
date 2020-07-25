//
// Created by LiHeng on 2020/7/12.
//

//DFS实现拓扑排序

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
            adjacency[vec[1]].push_back(vec[0]);
        for(int i=0; i<numCourses; ++i)
            if (dfs(i, flag, adjacency))
                return vector<int>();
        reverse(res.begin(), res.end()); //为什么要反序，思考下
        return res;
    }

    //返回true代表有向图有环，false代表无环
    bool dfs(int index, vector<int>& flag, vector<vector<int>>& adjacency){
        if(flag[index] == -1) return false;
        if(flag[index] == 1) return true;
        flag[index] = 1;
        for(auto j:adjacency[index]) //adjacency[index]里面存放的是学完index课程后可以学的其他课程
            if (dfs(j, flag, adjacency))
                return true;
        flag[index] = -1;
        res.push_back(index);
        return false;
    }
};

//可以用案例 3 [[0,1],[0,2],[1,2]] 理解过程



//BFS实现的拓扑排序
#include <queue>
class Solution1 {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> res;
        vector<int> indegrees(numCourses, 0); //入度记录
        vector<vector<int>> adjacency(numCourses, vector<int>());
        for(auto vec: prerequisites){
            indegrees[vec[0]]++;
            adjacency[vec[1]].push_back(vec[0]);
        }
        queue<int> q1;
        for(int i=0; i<numCourses; i++)
            if(indegrees[i] == 0)
                q1.push(i);
        while(!q1.empty()){
            int pre = q1.front();
            q1.pop();
            res.push_back(pre);
            numCourses -= 1;
            for(auto cur:adjacency[pre]){
                indegrees[cur]--;
                if(indegrees[cur] == 0)
                    q1.push(cur);
            }
        }
        return numCourses == 0?res:vector<int>();
    }
};