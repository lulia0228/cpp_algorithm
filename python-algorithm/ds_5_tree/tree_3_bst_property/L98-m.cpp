//
// Created by LiHeng on 2020/5/20.
//

//二叉查找树（BST）：根节点大于等于左子树所有节点，小于等于右子树所有节点。
//二叉查找树中序遍历有序。

#include <iostream>
#include <vector>
using  namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//方法1 利用了二叉搜索树的中序遍历性质
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        vector<int> res;
        inorderTree(root, res);
        for(int i=1; i<res.size(); ++i)
            if(res[i] <= res[i-1])
                return false;
        return true;
    }

    void inorderTree(TreeNode* root, vector<int> & res){
        if (root == NULL)
            return;
        inorderTree(root->left, res);
        res.push_back(root->val);
        inorderTree(root->right, res);
    }
};

//仍然是中序遍历，中序遍历的栈写法,相当于只把左节点入栈了，即每次遍历到左节点入栈，然后直接访问右节点不入栈

#include <stack>
class Solution1 {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> stack;
        long long inorder = (long long)INT_MIN - 1;

        while (!stack.empty() || root != nullptr) {
            while (root != nullptr) {
                stack.push(root);
                root = root -> left;
            }
            root = stack.top();
            stack.pop();
            // 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if (root -> val <= inorder) return false;
            inorder = root -> val;
            root = root -> right;
        }
        return true;
    }
};


//方法3  递归写法
//判断每个节点和父节点的关系
class Solution2 {
public:
    bool helper(TreeNode* root, long long lower, long long upper) {
        if (root == nullptr) return true;
        if (root -> val <= lower || root -> val >= upper) return false;
        return helper(root -> left, lower, root -> val) && helper(root -> right, root -> val, upper);
    }
    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);
    }
};

