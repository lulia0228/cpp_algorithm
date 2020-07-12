//
// Created by LiHeng on 2020/5/21.
//
#include <iostream>
#include <vector>
using  namespace std;

//方法一 DFS 对每个节点做DFS判断是否有环
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> flag(numCourses, 0);
        vector<vector<int>> adjacency(numCourses, vector<int>());
        for(auto vec: prerequisites)
            //adjacency[vec[1]].push_back(vec[0]);
            adjacency[vec[0]].push_back(vec[1]); //使用DFS方法，两种存放都可以
        for(int i=0; i<numCourses; ++i)
            if (!dfs(i, flag, adjacency))
                return false;
        return true;
    }

    bool dfs(int index, vector<int>& flag, vector<vector<int>>& adjacency){
        if(flag[index] == -1) return true;
        if(flag[index] == 1) return false;
        flag[index] = 1;
        for(auto j:adjacency[index]) //注意adjacency[index]里面存放的是index节点的所有邻接节点的索引，直接使用即可
            if (!dfs(j, flag, adjacency))
                return false;
        flag[index] = -1;
        return true;
    }
};

//方法2 同样是判断图中有无环存在  但是使用的是   拓扑排序+宽搜
#include <queue>
class Solution1 {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
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
            numCourses -= 1;
            for(auto cur:adjacency[pre]){
                indegrees[cur] --;
                if(indegrees[cur] == 0)
                    q1.push(cur);
            }
        }
        return numCourses==0;
    }
};


int main(){
    vector<int> v1 = {1,0};
    vector<vector<int>> v;
    v.push_back(v1);
    bool res = Solution().canFinish(2, v);
    cout << res << endl;
}