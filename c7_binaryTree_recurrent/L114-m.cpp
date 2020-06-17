//
// Created by LiHeng on 2020/5/20.
//

#include <iostream>
using  namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    void flatten(TreeNode* root) {
        while (root != NULL) {
            //左子树为 null，直接考虑下一个节点
            if (root->left == NULL) {
                root = root->right;
            } else {
                // 找左子树最右边的节点
                TreeNode* pre = root->left;
                while (pre->right != NULL) {
                    pre = pre->right;
                }
                //将原来的右子树接到左子树的最右边节点
                pre->right = root->right;
                // 将左子树插入到右子树的地方
                root->right = root->left;
                root->left = NULL;
                // 考虑下一个节点
                root = root->right;
            }
        }
    }
};