
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


//1 递归 前序遍历 DFS 效率高

class Solution {
public:
    vector<vector<int>> res;
    vector<int> temp;//防止反复初始化数组
    void dfs(TreeNode* root,int sum){
        int resum = sum-root->val;
        temp.push_back(root->val);
        if(resum == 0 && !root->left && !root->right)
            res.push_back(temp);
        if(root->left != NULL)
            dfs(root->left, resum);
        if(root->right != NULL)
            dfs(root->right, resum);
        temp.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(root == NULL) return res;
        dfs(root, sum);
        return res;
    }
};


//2 非递归写法 栈 前序遍历 效率低
#include <stack>
class Solution1 {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        if(root == NULL)
            return res;
        stack<pair<TreeNode*, vector<int>>> s1;
        s1.push(make_pair(root , vector<int> {root->val}));
        while(!s1.empty()){
            TreeNode* tem = s1.top().first;
            vector<int> cumulate = s1.top().second;
            s1.pop();
            int tmp_sum = 0;
            for (auto val:cumulate)
                tmp_sum += val;
            //访问到叶子节点时判断路径
            if(tem->left == NULL && tem->right == NULL && tmp_sum == sum)
                res.push_back(cumulate);
            //用的栈，右子树先进，才是前序遍历: 根->左->右
            if(tem->right != NULL){
                vector<int> r = cumulate;
                r.push_back(tem->right->val);
                s1.push(make_pair(tem->right,r));
            }
            if(tem->left != NULL){
                vector<int> l = cumulate;
                l.push_back(tem->left->val);
                s1.push(make_pair(tem->left,l));
            }
        }
        return res;
    }
};