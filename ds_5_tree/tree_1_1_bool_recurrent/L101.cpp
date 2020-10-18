

// 101 对称的二叉树

#include <iostream>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


//1 递归写法
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return ismirror(root,root);
    }

    bool ismirror(TreeNode* t1,TreeNode* t2){
        if(t1 == NULL&&t2 == NULL) //都为空
            return true;
        if(t1 == NULL||t2 == NULL)//有一个为空
            return false;
        if(t1->val != t2->val)
            return false;
        return ismirror(t1->left,t2->right)&&ismirror(t1->right,t2->left);
    }
};

//2 非递归写法:队列迭代 类似BFS
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <queue>
class Solution1 {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);
        while(!q.empty()){
            TreeNode* lt = q.front();
            q.pop();
            TreeNode* rt = q.front();
            q.pop();
            if(lt == NULL && rt == NULL) continue;
            if(lt == NULL || rt == NULL) return false;
            if(lt->val != rt->val) return false;
            q.push(lt->left);
            q.push(rt->right);
            q.push(lt->right);
            q.push(rt->left);
        }
        return true;
    }
};