
#include <iostream>
#include <vector>
using  namespace std;

//本题可约化为： 课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。
//思路：通过拓扑排序判断此课程安排图是否是 有向无环图(DAG) 。
//拓扑排序原理： 对 DAG 的顶点进行排序，使得对每一条有向边(u,v)，均有u（在排序记录中）比v先出现。
//亦可理解为对某点v而言，只有当v的所有源点均出现了，v才能出现。


//方法1 DFS 对每个节点做DFS判断是否有环
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> flag(numCourses, 0);
        vector<vector<int>> adjacency(numCourses, vector<int>());
        for(auto vec: prerequisites)
            adjacency[vec[1]].push_back(vec[0]); //这里注意是有向图
        for(int i=0; i<numCourses; ++i)
            if (dfs(i, flag, adjacency))
                return false;
        return true;
    }

    //返回true代表有向图 有环，false代表无环
    bool dfs(int index, vector<int>& flag, vector<vector<int>>& adjacency){
        if(flag[index] == -1) return false; //提前剪枝，说明以当前index为起始点的环检测前面已经做过了，而且是没有环的
        if(flag[index] == 1) return true;
        flag[index] = 1;
        for(auto j:adjacency[index]) //adjacency[index]里面存放的是学完index课程后可以学的其他课程
            if (dfs(j, flag, adjacency))
                return true;
        flag[index] = -1; //说明index起始检测没环,这句话必不可少：可以用案例3 [[0,1],[0,2],[1,2]] 理解
        return false;
    }
};

//方法2 同样是判断有向图中有无环存在  但是使用的是bfs实现拓扑排序
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
                indegrees[cur]--;
                if(indegrees[cur] == 0)
                    q1.push(cur);
            }
        }
        return numCourses == 0;
    }
};


int main(){
    vector<int> v1 = {1,0};
    vector<vector<int>> v;
    v.push_back(v1);
    bool res = Solution().canFinish(2, v);
    cout << res << endl;
}