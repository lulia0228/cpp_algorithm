

//二叉树的直径

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
    int get(TreeNode* Node) {
        if (Node == NULL) return 0;
        //l,r代表的是每个当前节点的左右子树的高度
        int l = get(Node -> left);
        int r = get(Node -> right);
        //每个节点，都会做一次比较
        res = max(res, l+r);
        return max(l, r) + 1;
    }

    int diameterOfBinaryTree(TreeNode* root) {
        get(root);
        return res;
    }

};