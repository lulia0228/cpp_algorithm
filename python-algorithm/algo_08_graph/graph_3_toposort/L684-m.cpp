
//唯一一道并查集的题目。

//方法1 并查集 :根据给定的边连接，按特殊规则建立起来的一棵树
#include <vector>
#include <iostream>
using  namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> rp(1001);
        int sz = edges.size();
        // 初始化各元素为单独的集合，代表（祖先）节点就是其本身
        for(int i=0;i<sz;i++)
            rp[i] = i;
        for(int j=0;j<sz;j++){
            // 找到边上两个节点所在集合的代表（祖先）节点
            int set1 = find(edges[j][0], rp);
            int set2 = find(edges[j][1], rp);
            if(set1 == set2)  //两个集合代表节点相同，说明出现环，返回答案
                return edges[j];
            else  //两个集合独立，合并集合。将前一个集合代表（祖先）节点戳到后一个集合代表（祖先）节点上
                rp[set1] = set2;
        }
        return {0, 0};
    }

    // 查找当前节点的祖先节点
    int find(int n, vector<int> &rp){
        int num = n;
        while(rp[num] != num)
            num = rp[num];
        return num;
    }

};

//方法2  DFS 每次拿掉一条边AB，然后看剩下的图中能否让节点A和B连通
//用DFS写 费了老大劲了
class Solution1 {
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

//效率很低
class Solution2 {
private:
    class UF {
    private:
        vector<int> id;
    public:
        UF(int N) {
            id = vector<int> (N + 1, 0);
            for (int i = 0; i < id.size(); i++) {
                id[i] = i;
            }
        }

        void uni(int u, int v) {
            int uID = find(u);
            int vID = find(v);
            if (uID == vID) {
                return;
            }
            for (int i = 0; i < id.size(); i++) {
                if (id[i] == uID) {
                    id[i] = vID;
                }
            }
        }

        int find(int p) {
            return id[p];
        }

        bool connect(int u, int v) {
            return find(u) == find(v);
        }

    };

public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int N = edges.size();
        UF uf(N+1);
        for (auto e : edges) {
            int u = e[0], v = e[1];
            if (uf.connect(u, v)) {
                return e;
            }
            uf.uni(u, v);
        }
        return {-1, -1};
    }
};
