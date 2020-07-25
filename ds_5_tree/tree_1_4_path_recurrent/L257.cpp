//
// Created by LiHeng on 2020/7/18.
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

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        string path ="";
        binaryTree(root,path,res);
        return res;
    }
    //string采用的是赋值传值的方式（不是引用或者指针），这样就意味着每次调用这个函数就会创建一个新的string，
    //并且还会在调用的时候把上一个string的值穿给他，这样就意味着每个函数中的path均不相同，
    //之所以提到这个，是因为如果返回路径要求用数组存储，需要有栈的弹出操作
    void binaryTree(TreeNode* root,string path,vector<string> &res){
        if(root == NULL)
            return;
        path.append(to_string(root->val));
        if(root->left == NULL && root->right == NULL)
            res.push_back(path);
        else
            path.append("->");
        if(root->left != NULL)
            binaryTree(root->left, path , res);
        if(root->right != NULL)
            binaryTree(root->right, path , res);
    }
};