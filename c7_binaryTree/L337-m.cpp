//
// Created by 李恒 on 2020/7/14.
//

//间隔遍历二叉树

#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//暴力递归 最后个案例没过
class Solution {
public:
    int rob(TreeNode* root) {
        if (root == NULL) return 0;
        int val1 = root->val;
        if (root->left != NULL) val1 += rob(root->left->left) + rob(root->left->right);
        if (root->right != NULL) val1 += rob(root->right->left) + rob(root->right->right);
        int val2 = rob(root->left) + rob(root->right);
        return max(val1, val2);
    }
};

//记忆化搜索，时间效率提高了，空间复杂度上去了
#include <unordered_map>
class Solution1 {
public:
    unordered_map<TreeNode*, int > um;
    int rob(TreeNode* root) {
        if (root == NULL) return 0;
        if(um.find(root) != um.end())
            return um[root];
        int val1 = root->val;
        if (root->left != NULL) val1 += rob(root->left->left) + rob(root->left->right);
        if (root->right != NULL) val1 += rob(root->right->left) + rob(root->right->right);
        int val2 = rob(root->left) + rob(root->right);
        int res = max(val1, val2);
        um[root] = res;
        return res;
    }
};