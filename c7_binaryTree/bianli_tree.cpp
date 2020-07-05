//
// Created by LiHeng on 2019/8/24.
//

//leetcode 144 94 145 二叉树前中后序遍历

#include <iostream>
#include <vector>
using namespace std ;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};

//前序遍历打印，递归实现
void preorder(TreeNode* node , vector<int> &res){
    if(node == NULL)  //递归终止条件
        return;
    res.push_back(node->val) ;
    preorder(node->left , res);
    preorder(node->right,res);
}

//中序遍历打印，递归实现
void inorder(TreeNode* node , vector<int> &res){
    if(node == NULL)  //递归终止条件
        return;
    inorder(node->left , res);
    res.push_back(node->val) ;
    inorder(node->right , res);
}

//后序遍历打印，递归实现
void postorder(TreeNode* node ,vector<int> &res){
    if(node == NULL)  //递归终止条件
        return;
    postorder(node->left,res);
    postorder(node->right,res);
    res.push_back(node->val) ;
}