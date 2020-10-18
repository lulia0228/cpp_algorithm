

//671. 二叉树中第二小的节点

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
    int findSecondMinimumValue(TreeNode* root) {
        //if (root == NULL) return -1; //非空树
        // -1 用于判定当前节点就是叶子节点
        if (root->left == NULL && root->right == NULL) return -1;
        int leftVal = root->left->val;
        int rightVal = root->right->val;
        if (leftVal == root->val) leftVal = findSecondMinimumValue(root->left);
        if (rightVal == root->val) rightVal = findSecondMinimumValue(root->right);
        if (leftVal != -1 && rightVal != -1) return min(leftVal, rightVal);
        if (leftVal != -1) return leftVal;
        return rightVal;
    }
};