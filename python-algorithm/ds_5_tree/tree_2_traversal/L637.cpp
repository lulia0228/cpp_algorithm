

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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        if(root ==  NULL) return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> tmp;
            int sz = q.size();
            long tmp_sum = 0;
            for(int i=0; i<sz; ++i){
                TreeNode* cur = q.front();
                q.pop();
                tmp_sum += cur->val;
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
            res.push_back(tmp_sum/(double)sz);
        }
        return res;
    }
};