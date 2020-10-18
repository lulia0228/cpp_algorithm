
//N叉树的最大深度
// 方法1 前序遍历DFS 递归
// 方法2：可用BFS层序遍历求层数

#include <iostream>
#include <vector>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;
    Node() {}

    Node(int _val) {
        val = _val;
    }
    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

// 这道题十分有助于理解递归  DFS系统栈递归
class Solution {
public:
    int maxDepth(Node* root) {
        if(root == NULL) return 0;
        vector<int> len_list(root->children.size(), 0);
        for(int i=0; i<len_list.size(); ++i)
            len_list[i] = maxDepth(root->children[i]);
        int res = 0;
        for(auto depth:len_list)
            res = max(res, depth);
        return res+1;
    }
};

//栈 DFS 迭代
#include <stack>
class Solution1 {
public:
    int maxDepth(Node* root) {
        int res = 0;
        if(root == NULL) return res;
        stack<pair<Node*,int>> s;
        s.push(make_pair(root,1));
        while(!s.empty()){
            Node* cur = s.top().first;
            int layer = s.top().second;
            s.pop();
            //当前节点是根节点的时候才更新
            if(cur->children.size() == 0)
                res = max(res, layer);
            for(int i=cur->children.size()-1; i>=0; --i){
                if (cur->children[i])
                    s.push(make_pair(cur->children[i], layer+1));
            }
        }
        return res;
    }
};

//层序遍历
#include <queue>
class Solution2 {
public:
    int maxDepth(Node* root) {
        int res = 0;
        if(root == NULL) return res;
        queue<Node*> q;
        q.push(root);
        int level = 0;
        while(!q.empty()){
            int sz = q.size();
            ++level;
            for(int i=0; i<sz; ++i){
                Node* cur = q.front();
                q.pop();
                if(cur->children.size() == 0)
                    res = max(res, level);
                for(auto node:cur->children){
                    if(node) q.push(node);
                }
            }
        }
        return res;
    }
};