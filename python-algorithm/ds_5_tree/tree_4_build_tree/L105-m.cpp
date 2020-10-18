
#include <iostream>
#include <vector>
using namespace std ;

struct  TreeNode {
    int val ;
    TreeNode *left ;
    TreeNode *right ;
    TreeNode(int x) : val(x) , left(NULL) , right(NULL) {}
};

//思想没有问题，就是4个数组 效率比较低
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int inorder_size = inorder.size();
        if(inorder_size == 0)
            return NULL;
        vector<int> preorder_left, preorder_right, inorder_left, inorder_right;
        //创建根节点
        TreeNode* head = new TreeNode(preorder[0]);
        //找到中序遍历根节点所在位置,存放于变量gen中
        int gen = 0;
        for(int i = 0 ;i < inorder_size ; i++){
            if(inorder[i] == preorder[0]){
                gen = i;
                break;
            }
        }
        // 左子树
        for(int i = 0; i < gen; i++){
            inorder_left.push_back(inorder[i]);
            preorder_left.push_back(preorder[i+1]);//先序第一个为根节点
        }
        // 右子树
        for(int i = gen + 1; i < inorder_size; i++){
            inorder_right.push_back(inorder[i]);
            preorder_right.push_back(preorder[i]);
        }
        //递归，执行上述步骤，区分子树的左、右子子树，直到叶节点
        head->left = buildTree(preorder_left, inorder_left);
        head->right = buildTree(preorder_right, inorder_right);

        return head;
    }
};

//传索引的方式 效率比上面快10倍
#include <unordered_map>
class Solution1 {
private:
    unordered_map<int, int> um;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int sz = preorder.size();
        // 构造哈希映射，帮助我们快速在中序遍历inorder中定位根节点，空间换时间的优化思想
        for(int i=0; i<sz; ++i)
            um[inorder[i]] = i;
        return myBuildTree(preorder, inorder, 0, sz-1, 0 , sz-1);
    }

    TreeNode* myBuildTree(vector<int>& preorder, vector<int>& inorder, int preorder_left,
                          int preorder_right, int inorder_left, int inorder_right){
        //递归终止条件
        if (preorder_left > preorder_right)
            return nullptr;
        // 前序遍历中的第一个节点就是根节点
        int preorder_root = preorder_left;
        // 在中序遍历中定位根节点
        int inorder_root = um[preorder[preorder_root]];
        // 先把根节点建立出来
        TreeNode* root = new TreeNode(preorder[preorder_root]);
        // 得到左子树中的节点数目
        int size_left_subtree = inorder_root - inorder_left;
        // 先序遍历中[preorder_left+1, preorder_left+size_left_subtree]的元素对应中序遍历[inorder_left, inorder_root-1]的元素
        root->left = myBuildTree(preorder, inorder, preorder_left+1, preorder_left+size_left_subtree, inorder_left, inorder_root-1);
        // 先序遍历中[preorder_left+size_left_subtree+1, preorder_right]的元素对应中序遍历[inorder_root + 1, inorder_right]的元素
        root->right = myBuildTree(preorder, inorder, preorder_left+size_left_subtree+1, preorder_right, inorder_root+1, inorder_right);
        return root;

    }
};

