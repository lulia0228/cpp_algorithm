
//左叶子节点的和

#include <iostream>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//递归，前序遍历
class Solution {
public:
    vector<int> temp;
    void dfs(TreeNode* root,TreeNode* father){
        if(father->left == root && !root->left && !root->right)
            temp.push_back(root->val);
        if(root->left != NULL)
            dfs(root->left, root);
        if(root->right != NULL)
            dfs(root->right, root);
    }

    int sumOfLeftLeaves(TreeNode* root) {
        int res = 0;
        if(root == NULL) return 0;
        dfs(root, root);
        for(auto item:temp)
            res += item;
        return res;
    }
};