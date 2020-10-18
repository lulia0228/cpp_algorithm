
#include <iostream>
#include <vector>

using namespace std;
//* Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//1 逆中序遍历，注意：中序遍历倒着来不是后序遍历
class Solution {
public:
    int sum = 0;
    TreeNode* convertBST(TreeNode* root) {
        if(root == NULL) return NULL;
        int sum = 0 ;
        Reverse_inorderTree(root);
        return root;
    }

    void Reverse_inorderTree(TreeNode* root){
        if (root == NULL) return;
        Reverse_inorderTree(root->right);
        sum += root->val;
        root->val = sum;
        Reverse_inorderTree(root->left);
    }
};

//或者这样写也可以
class Solution1 {
public:
    int cursum = 0;
    TreeNode* convertBST(TreeNode* root) {
        if(root == NULL)
            return NULL;
        convertBST(root->right);
        cursum += root->val;
        root->val = cursum;
        convertBST(root->left);

        return root;
    }
};

//2 中序遍历，需要先走完一遍获得总和，方便计算比当前节点值大的节点值得和

class Solution2 {
public:
    TreeNode* convertBST(TreeNode* root) {
        if(root == NULL)
            return NULL;
        int sum = 0;
        sumtree(root, sum); //所有节点和
        inordertree(root, sum);
        return root;
    }

    void sumtree(TreeNode* root, int& sum ){
        if (root == NULL)
            return ;
        sumtree(root->left, sum);
        sum += root->val;
        sumtree(root->right, sum);
    }

    void inordertree(TreeNode* root, int& sum ){
        if(root == NULL)
            return;
        inordertree(root->left, sum);
        sum = sum - root->val; //所有比当前节点大的节点值的和
        root->val = sum + root->val;//再加上原来节点的值
        inordertree(root->right, sum);
    }

};

