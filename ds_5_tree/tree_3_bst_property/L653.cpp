

#include <iostream>
#include <vector>
using namespace std;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};

//1  栈迭代中序遍历+哈希查找
#include <stack>
#include <unordered_set>
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        if(root == nullptr) return false;
        unordered_set<int> s;
        stack<TreeNode*> stk;
        while (!stk.empty() || root != nullptr) {
            while (root != nullptr) {
                stk.push(root);
                root = root -> left;
            }
            root = stk.top();
            stk.pop();
            if(s.find(k-root->val) != s.end())
                return true;
            s.insert(root->val) ;
            root = root -> right;
        }
        return false;
    }

};

//或者 因为是二叉查找树，用了哈希，任何遍历都可以 下面前序遍历也可以
class Solution1 {
public:
    bool findTarget(TreeNode* root, int k)  {
        if(root == NULL) return false;
        unordered_set<int> set1;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            TreeNode* cur = s.top();
            s.pop();
            if(set1.find(k-cur->val) != set1.end())
                return true;
            set1.insert(cur->val);
            if(cur->right != NULL )
                s.push(cur->right);
            if(cur->left != NULL )
                s.push(cur->left);
        }
        return false;
    }

};

// 2 中序遍历得到数组，然后对数组使用双指针
class Solution2 {
public:
    bool findTarget(TreeNode* root, int k) {
        if(root == NULL) return false;
        vector<int> nums;
        InorderTree(root, nums);
        int i=0, j=nums.size()-1;
        while(i<j){
            if (nums[i]+nums[j] == k)
                return true;
            else if (nums[i]+nums[j] > k)
                --j;
            else
                ++i;
        }
        return false;
    }

    void InorderTree(TreeNode* root, vector<int>& nums){
        if (root == NULL)
            return;
        InorderTree(root->left, nums);
        nums.push_back(root->val);
        InorderTree(root->right, nums);
    }

};
