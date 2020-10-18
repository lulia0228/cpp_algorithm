
//平衡二叉树 这道题不太好想到解法

#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


// 时间复杂度：O(n)
// 空间复杂度：O(logn) 极度不平衡为 O(n)

// 1 递归写法  前序遍历 DFS
class Solution {
public:
    bool flg = false;
    int get(TreeNode* Node) {
        if (Node == NULL) return 0;
        //l,r代表的是每个当前节点的左右子树的高度
        int l = 1 + get(Node -> left);
        int r = 1 + get(Node -> right);
        if (abs(l - r) > 1) {//每个节点的左右子树节点高度都做了比较
            flg = true;
        }
        return max(l, r);
    }

    bool isBalanced(TreeNode* root) {
        get(root);
        return !flg;
    }
};

//或者
class Solution1 {
public:
    bool flg = false;
    int get(TreeNode* Node) {
        if (Node == NULL) return 0;
        //l,r代表的是每个当前节点的左右子树的高度
        int l = get(Node -> left);
        int r = get(Node -> right);
        if (abs(l - r) > 1) {//每个节点的左右子树节点高度都做了比较
            flg = true;
        }
        return max(l, r) + 1;
    }

    bool isBalanced(TreeNode* root) {
        get(root);
        return !flg;
    }
};