

#include <iostream>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};

//常规办法
#include <vector>
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> nums;
        InorderTree(root, nums);
        int res = INT_MAX;
        for(int i=1; i<nums.size(); ++i)
            res = min(res, abs(nums[i]-nums[i-1]));
        return res;
    }

    void InorderTree(TreeNode* root,vector<int>& nums){
        if(root == NULL) return;
        InorderTree(root->left, nums);
        nums.push_back(root->val);
        InorderTree(root->right, nums);
    }
};

//边遍历，边比较
class Solution1 {
public:
    TreeNode* pre = NULL;
    int res = INT_MAX;
    int getMinimumDifference(TreeNode* root) {
        InorderTree(root);
        return res;
    }

    void InorderTree(TreeNode* root){
        if(root == NULL) return;
        InorderTree(root->left);
        if (pre != NULL) res = min(res, abs(root->val-pre->val));
        pre = root;
        InorderTree(root->right);
    }
};

//或者 栈迭代中序遍历
#include <stack>
class Solution2 {
public:
    int getMinimumDifference(TreeNode* root){
        int res =  INT_MAX;
        stack<TreeNode*> stk;
        TreeNode* pre = NULL;
        while (!stk.empty() || root != nullptr) {
            while (root != nullptr) {
                stk.push(root);
                root = root -> left;
            }
            root = stk.top();
            stk.pop();
            if(pre != NULL) res = min(res, abs(root->val-pre->val));
            pre = root;
            root = root -> right;
        }
        return res;
    }
};
