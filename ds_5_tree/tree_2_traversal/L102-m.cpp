

//队列的基本应用：广度优先遍历
//- 树： 层序遍历
//- 图： 无权图的最短路径 L279

//leetcode 102 二叉树层序遍历(从左到右)，如果想从右到左，可以先入队右子节点

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root ==  NULL) return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> tmp;
            int sz = q.size();
            for(int i=0; i<sz; ++i){
                TreeNode* cur = q.front();
                q.pop();
                tmp.push_back(cur->val);
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
            res.push_back(tmp);
        }
        return res;
    }
};

class  Solution1{
public:
    vector< vector<int> > levelOrder(TreeNode* root){
        vector< vector<int> > res ;
        if(root == NULL)
            return res ;
        queue< pair<TreeNode* , int> > q; //int 代表所在层数
        q.push(make_pair(root , 0));
        while(!q.empty()){
            TreeNode* node = q.front().first ;
            int level = q.front().second ;
            q.pop() ;
            if(level == res.size())
                res.push_back(vector<int> ());
            res[level].push_back(node->val) ;
            if(node->left)
                q.push(make_pair(node->left, level + 1));
            if(node->right)
                q.push(make_pair(node->right, level + 1));
        }
        return res ;
    }
};

int main(){
    return 0 ;
}


//练习题 leetcode 107 103 199