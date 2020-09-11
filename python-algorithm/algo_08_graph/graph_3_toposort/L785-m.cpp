//
// Created by LiHeng on 2020/7/12.
//
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

//思路：
//如果节点属于第一个集合，将其着为蓝色，否则着为红色。只有在二分图的情况下，
//可以使用贪心思想给图着色：一个节点为蓝色，说明它的所有邻接点为红色，它的邻接点的所有邻接点为蓝色，依此类推。

//DFS 递归栈
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int m = graph.size();
        vector<int> color(m, -1);
        for(int i=0; i<m; ++i){
            if(color[i] == -1 && !IsErFen(graph, i, 0, color))
                return false;
        }
        return true;
    }

    //每下探一层遍历的对象是当前节点的邻接节点
    bool IsErFen(vector<vector<int>>& graph, int curNode, int curColor, vector<int>& color){
        if (color[curNode] != -1)
            return  color[curNode] == curColor;
        color[curNode] = curColor;
        for(int nextNode: graph[curNode]){
            //if(!IsErFen(graph, nextNode, curColor^1, color))
            if(!IsErFen(graph, nextNode, 1-curColor, color))
                return false;
        }
        return true;
    }
};

//显式栈 stack
#include <stack>
class Solution1 {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int m = graph.size();
        vector<int> color(m, -1);
        for(int start=0; start<m; ++start){
            if (color[start] == -1){
                stack<int> s;
                s.push(start);
                color[start] = 0;
                while(!s.empty()){
                    int curNode = s.top();
                    s.pop();
                    for(int nextNode:graph[curNode]){
                        if(color[nextNode] == -1){
                            s.push(nextNode);
                            color[nextNode] = 1-color[curNode];
                        }
                        else{
                            if(color[nextNode] == color[curNode])
                                return false;
                        }
                    }
                }
            }
        }
        return true;
    }

};