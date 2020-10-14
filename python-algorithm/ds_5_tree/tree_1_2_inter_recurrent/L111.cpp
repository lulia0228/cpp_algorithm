//
// Created by 李恒 on 2020/7/14.
//

//二叉树的最小深度
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//1 递归写法，有点不太好理解
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        int leftH = minDepth(root->left);
        int rightH = minDepth(root->right);
        // 对当前节点而言，左子树为空，右子树不一定为空
        if(leftH == 0 )
            return rightH + 1;
        if(rightH == 0 )
            return leftH + 1;
        return min(leftH,rightH)+1;
    }
};

// 2 栈 前序遍历 DFS
#include <stack>
class Solution1 {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        stack<pair<TreeNode*, int>> s1;
        s1.push(make_pair(root , 1));
        int res = INT_MAX;
        while(!s1.empty()){
            TreeNode* tem = s1.top().first;
            int depth = s1.top().second;
            s1.pop();
            //访问到叶子节点时更新最小深度
            if(tem->left == NULL && tem->right == NULL)
                res = min(res,depth);
            if(tem->left != NULL)
                s1.push(make_pair(tem->left,depth+1));
            if(tem->right != NULL)
                s1.push(make_pair(tem->right,depth+1));
        }
        return res;

    }
};


//3 队列 层序遍历 BFS
#include <queue>
class Solution2 {
public:
    int minDepth(TreeNode* root) {
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
                if(tmp->left == NULL && tmp->right == NULL )
                    return level;
                if(tmp->left != NULL)
                    q.push(tmp->left);
                if(tmp->right != NULL)
                    q.push(tmp->right);
            }
        }
        return 0;
    }
};