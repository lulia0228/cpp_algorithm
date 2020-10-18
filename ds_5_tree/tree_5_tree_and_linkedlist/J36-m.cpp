
#include <iostream>
using namespace std ;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
private:
    Node* pre;
    Node* head;
public:
    Node* treeToDoublyList(Node* root) {
        if (root == NULL) return NULL;
        InorderTree(root);
        //最终要返回的是双向循环链表，所以下面将头尾连接起来
        head->left = pre;
        pre->right = head;
        return head;
    }
    //下面操作之后，根节点不是循环双向链表的头节点。
    void InorderTree(Node* root){
        if (root == NULL)
            return;
        InorderTree(root->left);
        if(pre != NULL){
            pre->right = root;
            root->left = pre;
        }
        else
            head = root;
        //root->left = pre;
        pre = root;
        InorderTree(root->right);
    }
};