//
// Created by 李恒 on 2020/7/14.
//
//路径总和：判断是否存在根到叶子节点的一条路径的和为某数

#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


//1  递归写法
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) return false;
        if (root->left == NULL && root->right == NULL && root->val == sum) return true;
        return hasPathSum(root->left, sum-root->val) || hasPathSum(root->right, sum-root->val);
    }
};

//2  非递归写法 ：栈 DFS遍历
#include <stack>
class Solution1 {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL)
            return false;
        stack<pair<TreeNode*, int>> s1;
        s1.push(make_pair(root , root->val));
        while(!s1.empty()){
            TreeNode* tem = s1.top().first;
            int cumulate = s1.top().second;
            s1.pop();
            //访问到叶子节点时判断路径
            if(tem->left == NULL && tem->right == NULL && cumulate == sum)
                return true;
            //用的栈，右子树先进，才是前序遍历: 根->左->右
            if(tem->right != NULL)
                s1.push(make_pair(tem->right,cumulate+tem->right->val));
            if(tem->left != NULL)
                s1.push(make_pair(tem->left,cumulate+tem->left->val));
        }
        return false;

    }
};

//或者
class Solution2 {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL)
            return false;
        stack<pair<TreeNode*, int>> s1;
        s1.push(make_pair(root , root->val));
        while(!s1.empty()){
            TreeNode* tem = s1.top().first;
            int cumulate = s1.top().second;
            s1.pop();
            //访问到叶子节点时判断路径
            if(tem->left == NULL && tem->right == NULL && cumulate == sum)
                return true;
            //用的栈，左子树先进，好像也不是后序遍历: 根->右->左
            if(tem->left != NULL)
                s1.push(make_pair(tem->left,cumulate+tem->left->val));
            if(tem->right != NULL)
                s1.push(make_pair(tem->right,cumulate+tem->right->val));
        }
        return false;

    }
};