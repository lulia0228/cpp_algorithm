//
// Created by LiHeng on 2020/4/19.
//

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
    //一定要搞明白二叉树递归走法到底是怎么遍历的？？？
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        int max_left_depth = maxDepth(root->left);
        int max_right_depth = maxDepth(root->right);
        return max(max_left_depth , max_right_depth) + 1;
    }
};