//
// Created by LiHeng on 2020/4/19.
//

//104 二叉树的深度，可以去对比下最小平方数和279那道题

#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

//1 递归写法 前序遍历 DFS
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        int max_left_depth = maxDepth(root->left);
        int max_right_depth = maxDepth(root->right);
        return max(max_left_depth , max_right_depth) + 1;
    }
};


//2 非递归写法 层序遍历 BFS
#include <queue>
class Solution1 {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        int level = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            ++level;
            for(int i=0; i<sz; ++i){
                TreeNode* tmp = q.front();
                q.pop();
                if(tmp->left != NULL)
                    q.push(tmp->left);
                if(tmp->right != NULL)
                    q.push(tmp->right);
            }
        }
        return level;
    }
};

//3 非递归写法 前序遍历 DFS
#include <stack>
class Solution2 {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        stack<pair<TreeNode*, int>> s;
        s.push(make_pair(root,1));
        int level = 0;
        while(!s.empty()){
            pair<TreeNode*, int> cur = s.top();
            s.pop();
            TreeNode* curNode = cur.first;
            int curLev = cur.second;
            if(curNode != NULL){
                level = max(level, curLev);
                s.push(make_pair(curNode->left, curLev+1));
                s.push(make_pair(curNode->right, curLev+1));
            }
        }
        return level;
    }
};

// 或者下面这样写也可以
#include <stack>
class Solution3 {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        stack<pair<TreeNode*, int>> s;
        s.push(make_pair(root,1));
        int level = 0;
        while(!s.empty()){
            pair<TreeNode*, int> cur = s.top();
            s.pop();
            TreeNode* curNode = cur.first;
            int curLev = cur.second;
            if(curNode->left == NULL && curNode->right == NULL)
                level = max(level, curLev);
            if(curNode->left != NULL)
                s.push(make_pair(curNode->left, curLev+1));
            if(curNode->right != NULL)
                s.push(make_pair(curNode->right, curLev+1));
        }
        return level;
    }
};

