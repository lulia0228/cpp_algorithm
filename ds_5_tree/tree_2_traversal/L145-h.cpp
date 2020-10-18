
//二叉树的后序遍历

#include <iostream>
#include <cassert>
#include <stack>
#include <vector>
using namespace std ;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};


// 1 递归写法
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorder(root, res);
        return res;
    }
    //后序遍历打印，递归实现
    void postorder(TreeNode* node ,vector<int> &res){
        if(node == NULL)  //递归终止条件
            return;
        postorder(node->left,res);
        postorder(node->right,res);
        res.push_back(node->val) ;
    }
};


// 栈迭代，二叉树前中后三种遍历的统一写法
struct Command{
    string s; // go print
    TreeNode* node ;
    Command(string s , TreeNode* node ): s(s) , node(node){}
};

class Solution1{
public:
    vector<int> postorderTraversal(TreeNode* root){
        vector<int> res ;
        if(root == NULL)
            return res;
        stack<Command> stack1 ;
        stack1.push(Command("go" ,root ));

        while(!stack1.empty()){
            Command command = stack1.top() ;
            stack1.pop() ;
            if(command.s == "print")
                res.push_back(command.node->val);
            else{ //进栈操作，注意3个的顺序
                assert( command.s == "go") ;
                stack1.push(Command("print", command.node));
                if(command.node->right) //判断如果当前节点的右子节点存在
                    stack1.push(Command("go", command.node->right));
                if(command.node->left) //判断如果当前节点的左子节点存在
                    stack1.push(Command("go", command.node->left));
            }
        }
        return  res ;
    }
};

int main(){
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);
    TreeNode* layer1_l = root->left;
    layer1_l->right = new TreeNode(6);
    TreeNode* layer1_r = root->right;
    layer1_r->left = new TreeNode(4);
    layer1_r->left->right = new TreeNode(0);

    vector<int> res = Solution1().postorderTraversal(root);
    for(auto i:res)
        cout << i << "\t";

    return 0;
}

//  6	1	0	4	3	2
//                   2
//                 /   \
//                1     3
//                 \   /
//                  6 4
//                     \
//                      0