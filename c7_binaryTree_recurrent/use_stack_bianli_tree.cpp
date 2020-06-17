//
// Created by LiHeng on 2019/8/10.


//非递归方式实现的二叉树遍历
//讲递归和栈的关系 leetcode 144 94 145 二叉树前中后序遍历
//结合栈的特点，理解递归的运行原理，每层执行的原理
//前序遍历的递归实现
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

struct Command{
    string s; // go print
    TreeNode* node ;
    Command(string s , TreeNode* node ): s(s) , node(node){}
};

//二叉树遍历的非递归实现
class Solution{
    vector<int> preorderTraversal(TreeNode* root){
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
            else{ //进栈操作，注意3个的顺序。     后进先出
                assert( command.s == "go") ;
                if(command.node->right) //判断如果当前节点的右子节点存在
                    stack1.push(Command("go", command.node->right));
                if(command.node->left) //判断如果当前节点的左子节点存在
                    stack1.push(Command("go", command.node->left));
                stack1.push(Command("print", command.node));
            }
        }
        return  res ;
    }

    vector<int> inorderTraversal(TreeNode* root){
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
            else{ //进栈操作，注意3个的顺序。     后进先出
                assert( command.s == "go") ;
                if(command.node->right) //判断如果当前节点的右子节点存在
                    stack1.push(Command("go", command.node->right));
                stack1.push(Command("print", command.node));
                if(command.node->left) //判断如果当前节点的左子节点存在
                    stack1.push(Command("go", command.node->left));
            }
        }
        return  res ;
    }

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
            else{ //进栈操作，注意3个的顺序。     后进先出
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
    return 0;
}

//练习题 leetcode 341