

//leetcode 103 二叉树锯齿形遍历

#include <iostream>
#include <cassert>
#include <queue>
#include <vector>
using namespace std ;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root ==  NULL) return res;
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        while(!q.empty()){
            vector<int> tmp;
            int sz = q.size();
            ++level;
            for(int i=0; i<sz; ++i){
                TreeNode* cur = q.front();
                q.pop();
                tmp.push_back(cur->val);
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
            if (level%2 == 0)
                reverse(tmp.begin(), tmp.end());
            res.push_back(tmp);
        }
        return res;
    }
};