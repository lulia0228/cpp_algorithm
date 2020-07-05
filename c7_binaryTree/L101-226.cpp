//
// Created by liheng on 19-9-11.
//

#include <iostream>
#include <vector>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};


class Solution{
private:
    vector<int> preorder_list ;
public:
    // 二叉树前序遍历 根节点，再到左节点，最后到右节点 递归写法
    vector<int> preorderTraversal(TreeNode* root){
        if(root == NULL)
            return preorder_list ;
        preorder_list.push_back(root->val);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
        return preorder_list ;
    }

    //leetcode 226  翻转二叉树
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL)
            return NULL;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root ;
    }

    //判断一个二叉树是否对称 L101
    //若一个二叉树root是镜像对称的，则与克隆体rootcopy有：
        //根节点相同
        //root每个右子树与rootcopy左子树镜像对称
        //root每个左子树与rootcopy右子树镜像对称

    bool isSymmetric(TreeNode* root) {
        return ismirror(root,root);
    }

    bool ismirror(TreeNode* t1,TreeNode* t2)
    {
        if(t1==NULL && t2==NULL) //都为空
            return true;
        if(t1==NULL || t2==NULL)//有一个为空
            return false;
        if(t1->val==t2->val)
            return ismirror(t1->left,t2->right)&&ismirror(t1->right,t2->left);
        else
            return false ;
    }

};