

//687. 最长同值路径

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
    int res = 0;
    int get(TreeNode* root) {
        if (root == NULL) return 0;
        //这里l,r代表的是每个当前节点的左右子树的连续层个数,和113 543 两道题有区别
        int left = get(root->left);
        int right = get(root->right);
        //每个节点，都会做一次比较
        int leftPath = root->left != NULL && root->left->val == root->val? left+1 : 0;
        int rightPath = root->right != NULL && root->right->val == root->val? right+1 : 0;
        res = max(res, leftPath + rightPath);
        return max(leftPath, rightPath);
    }

    int longestUnivaluePath(TreeNode* root) {
        get(root);
        return res;
    }

};