

//返回数字1-n可以构建的所有二叉搜索树

#include <iostream>
#include <vector>
using namespace std;
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if(n < 1 ) return vector<TreeNode*>();
        return helper(1, n);
    }

    vector<TreeNode*> helper(int start, int end){
        vector<TreeNode*> list;
        if(start > end){
            // 如果当前子树为空，不加null行吗？
            list.push_back(NULL);
            return list;
        }

        for(int i = start; i <= end; i++){
            // 想想为什么这行不能放在这里，而放在下面？
            // TreeNode* root = new TreeNode(i);
            vector<TreeNode*> left = helper(start, i-1);
            vector<TreeNode*> right = helper(i+1, end);

            // 固定左孩子，遍历右孩子
            for(TreeNode* l : left){
                for(TreeNode* r : right){
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    list.push_back(root);
                }
            }
        }
        return list;
    }
};

//类似回溯的，每层都有可选的迭代对象
//先参考108题 如何从1~n构建平衡二叉搜索树，再去理解要构造多棵二叉搜索树