

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

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        mypreorder(root, res);
        return res;
    }

    //前序遍历打印，递归实现
    void mypreorder(Node* node , vector<int> &res){
        if(node == NULL)  //递归终止条件
            return;
        res.push_back(node->val) ;
        for(auto point:node->children)
            mypreorder(point,res);
    }
};

//非递归写法
#include <stack>
class Solution1 {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        if(root == NULL) return res;
        stack<Node*> s;
        s.push(root);
        while(!s.empty()){
            Node* cur = s.top();
            s.pop();
            if(cur == NULL) continue;
            res.push_back(cur->val);
            for(int i=cur->children.size()-1; i>=0; --i)
                s.push(cur->children[i]);
        }
        return res;
    }
};