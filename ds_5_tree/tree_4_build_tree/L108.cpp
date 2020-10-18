

#include <iostream>
#include <vector>
using  namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//递归树，要注意每次递归返回的类型是什么
class Solution {
public:
    TreeNode* DFS(vector<int>& nums, int start, int end){
        if(start > end){
            return NULL;
        }
        int mid = start + (end-start)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = DFS(nums, start, mid-1);
        root->right = DFS(nums, mid+1, end);
        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return DFS(nums, 0, nums.size()-1);
    }

};