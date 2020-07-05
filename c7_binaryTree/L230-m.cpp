//
// Created by LiHeng on 2020/4/19.

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


//上面的中序遍历，可以在遍历到k个元素时候就停止，速度会加快。只是这个逻辑，写起来稍微有点难啊
class Solution1 {
public:
    int kthSmallest(TreeNode* root, int k){
        if(root == NULL || k <= 0)
            return NULL ;
        return BstNode(root, k)->val;
    }

    TreeNode* BstNode(TreeNode* cur , int &k){
        TreeNode* target = NULL ;
        if(cur->left != NULL)
            target = BstNode(cur->left , k);
        if(target == NULL){
            if(k == 1)//如果当前节点刚好是第k个
                target = cur ;
            k--;//相当于打印当前节点
        }
        if(target == NULL && cur->right != NULL) //再看当前节点的右子节点
            //target == NULL是一定要有的，因为不为空说明找到了，这句话不再执行，递归结束
            target = BstNode(cur->right , k);
        return target ;
    }
};


//迭代的方法， 借助栈，完成树的深度优先遍历
#include <stack>
class Solution2 {
public:
    int kthSmallest(TreeNode* root, int k) {
        //迭代
        stack<TreeNode*>  stk;
        int res;
        int n = 0;
        TreeNode* cur = root;
        while(!stk.empty() || cur){
            while(cur){
                stk.push(cur);
                cur = cur->left;
            }
            cur = stk.top();
            stk.pop();
            n++;
            if(n == k)
                return cur->val;
            cur = cur->right;
        }
        return 0;//这里似乎是必须加一句否则会报错
    }
};