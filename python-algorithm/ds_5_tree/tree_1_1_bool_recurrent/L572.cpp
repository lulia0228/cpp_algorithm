

#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(s == NULL || t == NULL) return false;
        return DoesTree1HaveTree2(s,t)||isSubtree(s->left, t)||isSubtree(s->right, t);
        // bool result = false ;
        // if(s->val == t->val )
        //     result = DoesTree1HaveTree2(s,t);
        // if(!result)
        //     result = isSubtree(s->left, t);
        // if(!result)
        //     result = isSubtree(s->right, t);
        // return result ;
    }

    //判断2棵树是否相等
    bool DoesTree1HaveTree2(TreeNode* pRoot1, TreeNode* pRoot2){
        if(pRoot1==NULL && pRoot2==NULL)  //两个都是空
            return true ;
        if(pRoot1==NULL || pRoot2 == NULL) //有一个为空
            return false ;
        if(pRoot1->val != pRoot2->val )//都不为空，且值不相等
            return false;
        return DoesTree1HaveTree2(pRoot1->left, pRoot2->left) &&
               DoesTree1HaveTree2(pRoot1->right, pRoot2->right);
    }

};