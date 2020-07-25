//
// Created by 李恒 on 2020/7/16.
//

//513. 找树左下角的值

#include <iostream>
#include <cassert>
#include <queue>
using namespace std ;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            root = q.front();
            q.pop();
            if(root->right)
                q.push(root->right);
            if(root->left)
                q.push(root->left);
        }
        return root->val;
    }
};