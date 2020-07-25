//
// Created by LiHeng on 2020/7/18.
//

#include <iostream>
#include <vector>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};

//写法一 和105一样，用4个数组效率低，下面改用索引
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int postorder_size = postorder.size();
        if(postorder_size == 0)
            return NULL;
        TreeNode* head = new TreeNode(postorder[postorder_size-1]);
        //在中序遍历中找到根节点的位置
        int gen = 0;
        for(int i = 0; i < postorder_size ; i++ ){
            if(inorder[i] == postorder[postorder_size-1]){
                gen = i ;
                break;
            }
        }
        vector<int> in_left,in_right,pos_left,pos_right;
        //左子树
        for(int i=0 ;i<gen;i++){
            in_left.push_back(inorder[i]);
            pos_left.push_back(postorder[i]);
        }
        //右子树
        for(int i=gen+1 ;i<postorder_size;i++){
            in_right.push_back(inorder[i]);
            pos_right.push_back(postorder[i-1]);
        }

        head->left = buildTree(in_left,pos_left);
        head->right = buildTree(in_right,pos_right);

        return head;
    }
};

//写法2  传索引 效率快多了
#include <unordered_map>
class Solution1 {
private:
    unordered_map<int, int> um;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int sz = inorder.size();
        // 构造哈希映射，帮助我们快速在中序遍历inorder中定位根节点，空间换时间的优化思想
        for(int i=0; i<sz; ++i)
            um[inorder[i]] = i;
        return myBuildTree(postorder, inorder, 0, sz-1, 0 , sz-1);
    }

    TreeNode* myBuildTree(vector<int>& postorder, vector<int>& inorder, int postorder_left,
                          int postorder_right, int inorder_left, int inorder_right){
        //递归终止条件
        if (postorder_left > postorder_right)
            return nullptr;
        // 前序遍历中的第一个节点就是根节点
        int postorder_root = postorder_right;
        // 在中序遍历中定位根节点
        int inorder_root = um[postorder[postorder_root]];
        // 先把根节点建立出来
        TreeNode* root = new TreeNode(postorder[postorder_root]);
        // 得到左子树中的节点数目
        int size_left_subtree = inorder_root - inorder_left;
        // 后序遍历中[preorder_left, preorder_left+size_left_subtree-1]的元素对应中序遍历[inorder_left, inorder_root-1]的元素
        root->left = myBuildTree(postorder, inorder, postorder_left, postorder_left+size_left_subtree-1, inorder_left, inorder_root-1);
        // 后序遍历中[preorder_left+size_left_subtree, preorder_right-1]的元素对应中序遍历[inorder_root+1, inorder_right]的元素
        root->right = myBuildTree(postorder, inorder, postorder_left+size_left_subtree, postorder_right-1, inorder_root+1, inorder_right);
        return root;

    }
};