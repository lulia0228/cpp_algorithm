//
// Created by 李恒 on 2020/7/14.
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

class Solution{
public:
    //在递归中又嵌套了一个递归
    int pathSum(TreeNode* root , int sum){
        if(root == NULL)
            return 0 ;
        // 对于每个节点考虑三种情况：1.路径包含这个节点 2.路径不包含这个节点，以当前节点的左子节点开头
        // 3.路径不包含这个节点，以当前节点的右子节点开头
        int res = findPath(root , sum );
        res += pathSum(root->left , sum );
        res += pathSum(root->right , sum );
        return res ;
    }

private:
    // 在以node为根节点的二叉树中寻找包含node的路径，和为sum 返回路径个数
    // 这里要注意的是，路径并不是以叶子节点结尾，所以写法逻辑和前面的案例不一样
    int findPath(TreeNode* node , int sum){
        if(node == NULL)
            return 0 ;
        int res = 0 ;
        if(node->val == sum )
            res += 1 ;
        res +=  findPath(node->left , sum - node->val);
        res +=  findPath(node->right , sum - node->val);
        return res ;
    }
};