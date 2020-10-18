
#include <iostream>
#include <vector>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};

// 题目要求不使用额外的空间
// (1)递归栈不能算吧 （2）用来装返回值的数组不能算
// 严格来讲下面空间复杂度，中间可能有开辟额外空间，不算O(1)
// 一定要O(1)空间复杂度的话，就做2次遍历，第一次记载下最大出现次数，第二次按照最大次数存储众数

class Solution {
public:
    int tmp_cnt = 1;
    int final_cnt = 1;
    TreeNode* pre = NULL;
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        InorderTree(root, res);
        return res;
    }

    void InorderTree(TreeNode* root, vector<int>& nums){
        if(root == NULL) return;
        InorderTree(root->left, nums);
        if(pre){
            if(root->val == pre->val)
                ++tmp_cnt;
            else
                tmp_cnt = 1;
        }
        if (tmp_cnt > final_cnt){
            final_cnt = tmp_cnt;
            nums.clear();
            nums.push_back(root->val);
        }
        else if(tmp_cnt == final_cnt)
            nums.push_back(root->val);
        pre = root;
        InorderTree(root->right, nums);
    }
};