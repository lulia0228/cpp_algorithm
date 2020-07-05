//
// Created by LiHeng on 2020/4/28.
//
#include <iostream>
#include <vector>

using namespace std;
//* Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if(root == NULL)
            return NULL;
        int sum = 0;
        sumtree(root, sum); //所有节点和
        inordertree(root, sum);
        return root;
    }

    void sumtree(TreeNode* root, int& sum ){
        if (root == NULL)
            return ;
        sumtree(root->left, sum);
        sum += root->val;
        sumtree(root->right, sum);
    }

    void inordertree(TreeNode* root, int& sum ){
        if(root == NULL)
            return;
        inordertree(root->left, sum);
        sum = sum - root->val; //所有比当前节点大的节点值的和
        root->val = sum + root->val;//再加上原来节点的值
        inordertree(root->right, sum);
    }

};

//更简单的做法，因为正常中序遍历，需要知道所有节点的和，才能确定比当前节点大的节点值之和
//现在转换下思路，把中序遍历倒过来，注意中序遍历倒过来不是后序遍历。
class Solution1 {
public:
    int cursum = 0;
    TreeNode* convertBST(TreeNode* root) {
        if(root == NULL)
            return NULL;
        convertBST(root->right);
        cursum += root->val;
        root->val = cursum;
        convertBST(root->left);

        return root;
    }
};