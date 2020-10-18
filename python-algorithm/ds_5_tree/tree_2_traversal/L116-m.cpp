
#include <iostream>
#include <queue>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node() : val(0), left(NULL), right(NULL), next(NULL) {}
    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}
    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
    Node* connect(Node* root) {
        if(root == NULL)
            return NULL;
        queue<Node*> q;
        q.push(root);
        int index = 0;
        while(!q.empty()){
            Node* cur = q.front();
            q.pop();
            index++;
            int flag = (index+1)&index; //注意如果在下面判断条件中直接用需要在表达式外面加个括号
            if (flag == 0)
                cur->next = NULL;
            else
                cur->next = q.front();
            if(cur->left!=NULL)
                q.push(cur->left);
            if(cur->right!=NULL)
                q.push(cur->right);
        }
        return root;
    }

};

//我的写法
class Solution1 {
public:
    Node* connect(Node* root) {
        if(root == NULL)
            return NULL;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()){
            int sz = q.size();
            int tmp_cnt = 0;
            for(int i=0; i<sz; ++i){
                Node* cur = q.front();
                q.pop();
                ++tmp_cnt;
                if (tmp_cnt == sz)
                    cur->next = NULL;
                else
                    cur->next = q.front();
                if(cur->left!=NULL)
                    q.push(cur->left);
                if(cur->right!=NULL)
                    q.push(cur->right);
            }
        }
        return root;
    }

};