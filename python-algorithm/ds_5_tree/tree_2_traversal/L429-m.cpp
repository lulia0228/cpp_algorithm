
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

#include <queue>
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        if(root == NULL) return res;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            vector<int> tmp;
            for(int i=0; i<sz; ++i){
                Node* cur = q.front();
                q.pop();
                tmp.push_back(cur->val);
                for(auto node:cur->children){
                    if(node) q.push(node);
                }
            }
            res.push_back(tmp);
        }
        return res;
    }
};