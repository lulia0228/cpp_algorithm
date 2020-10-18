
//翻转二叉树

#include <iostream>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};

//1 递归写法
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL)
            return NULL;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root ;
    }
};


#include <queue>
//2 非递归写法:队列迭代 类似BFS
class Solution1 {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return NULL;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* tmp = q.front();
            q.pop();
            swap(tmp->left, tmp->right);
            if(tmp->left != NULL) //顺序可以颠倒，无影响
                q.push(tmp->left);
            if(tmp->right != NULL)
                q.push(tmp->right);
        }
        return root;
    }
};


//2 非递归写法:栈迭代 类似DFS
#include <stack>
class Solution2 {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return NULL;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            TreeNode* tmp = s.top();
            s.pop();
            //swap(tmp->left, tmp->right);
            if(tmp->left != NULL)
                s.push(tmp->left);
            if(tmp->right != NULL)
                s.push(tmp->right);
            swap(tmp->left, tmp->right);
        }
        return root;
    }
};