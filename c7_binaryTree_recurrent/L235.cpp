//
// Created by LiHeng on 2020/4/19.
//

//给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
//思路：前提是二叉搜索树，这道题就变简单了只要2个给出节点的值分布在根节点的两侧，根节点就是最近公共祖先。递归构建新的根节点就可以找到。
#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL)
            return root;
        if(p->val < root->val && q->val < root->val)
            return lowestCommonAncestor(root->left , p , q);
        if(p->val > root->val && q->val > root->val)
            return lowestCommonAncestor(root->right , p , q);
        return root ;
    }
};

