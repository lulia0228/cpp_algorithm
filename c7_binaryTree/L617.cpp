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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2)
    {
        if(!t1)
            return t2;
        if(!t2)
            return t1;
        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
};


//下面这个迭代的效率没有上面递归的好
#include <stack>
#include <queue>
class Solution1 {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(t1 == NULL)
            return t2;
        stack<pair<TreeNode*, TreeNode*>> stk;
        stk.push(pair<TreeNode*, TreeNode*> (t1,t2));
        while(!stk.empty()){
            pair<TreeNode*,TreeNode*> tmp = stk.top(); //使用queue也是可以的，对应修改为.front()
            stk.pop();
            if(tmp.first == NULL || tmp.second == NULL)
                continue;
            tmp.first->val += tmp.second->val;
            if (tmp.first->left == NULL)//t1的左子树
                tmp.first->left = tmp.second->left;
            else
                stk.push(pair<TreeNode*, TreeNode*>(tmp.first->left,tmp.second->left));

            if (tmp.first->right == NULL)//t1的右子树
                tmp.first->right = tmp.second->right;
            else
                stk.push(pair<TreeNode*, TreeNode*>(tmp.first->right,tmp.second->right));
        }
        return t1;
    }
};
