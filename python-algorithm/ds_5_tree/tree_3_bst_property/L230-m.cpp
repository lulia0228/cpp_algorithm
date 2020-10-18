
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

//递归完成树的深度优先搜索
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        if(root == NULL)
            return NULL;
        vector<int> vec; //这里在不确定节点值是什么类型时候，最后在vector里面直接存节点，最后取节点val就好了
        midordertree(root, vec);
        return vec[k-1];
    }

    void midordertree(TreeNode* root , vector<int>& vec){
        if (root == NULL) //这种写法作为递归终止，千万不能利用while(root != NULL)来执行下面的语句，因为是死循环
            return;
        midordertree(root->left, vec);
        vec.push_back(root->val);
        midordertree(root->right, vec);
    }
};


//栈迭代 仍然是中序遍历
#include <stack>
class Solution1 {
public:
    int kthSmallest(TreeNode* root, int k) {
        //if(root == nullptr) return res;
        stack<TreeNode*> stack;
        int cnt = 0;
        while (!stack.empty() || root != nullptr) {
            while (root != nullptr) {
                stack.push(root);
                root = root -> left;
            }
            root = stack.top();
            stack.pop();
            ++cnt;
            if (cnt == k) return root->val;
            root = root -> right;
        }
        return 1;//符合int返回类型，加一句
    }

};