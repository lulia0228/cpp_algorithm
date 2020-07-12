//
// Created by LiHeng on 2020/7/12.
//

//唯一一道并查集的题目

//方法1 并查集
//方法2  DFS 每次拿掉一条边AB，然后看剩下的图中能否让节点A和B连通

//用DFS写 费了老大劲了
#include <vector>
#include <iostream>
using  namespace std;
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int m = edges.size();
        vector<vector<int>> res;
        vector<vector<int>> graph(m, vector<int>());
        build_graph(edges, graph);
        for(int i=0; i<m; ++i){
            vector<vector<int>> tmp_graph = graph;
            vector<bool> visited(m, false);
            deleEle(tmp_graph[edges[i][0]-1], edges[i][1]-1);
            deleEle(tmp_graph[edges[i][1]-1], edges[i][0]-1);

            if(dfs(tmp_graph, edges[i][0]-1, edges[i][1]-1, visited)){
                //cout << "add res "<< edges[i][0]<<edges[i][1]<<endl;
                res.push_back(edges[i]);
            }

        }
        //return res[-1]; //c++中没有-1索引的用法
        return res[res.size()-1];

    }

    void build_graph(vector<vector<int>>& edges, vector<vector<int>>& graph){
        for(auto p:edges){
            graph[p[0]-1].push_back(p[1]-1);
            graph[p[1]-1].push_back(p[0]-1);
        }
    }

    void deleEle(vector<int>& a, int target){
        for(vector<int>::iterator it=a.begin(); it != a.end(); ){
            if(*it == target)
                it = a.erase(it);
            else
                ++it;
        }
    }

    bool dfs(vector<vector<int>>& graph, int start, int target, vector<bool>& visited){
        if (start == target) return true;
        visited[start] = true;
        if(graph[start].size() != 0){
            for(int nextNode:graph[start]){
                //记住啊，如果要按下面的条件写在一起，!visited[nextNode] 必须要在前面
                if(!visited[nextNode] && dfs(graph, nextNode, target, visited))
                    return true;
            }
        }
        return false;
    }

};

int main(){
    vector<vector<int>> v = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};
    vector<int> res = Solution().findRedundantConnection(v);
    for (auto i:res)
            cout<< i << '\t';
}

