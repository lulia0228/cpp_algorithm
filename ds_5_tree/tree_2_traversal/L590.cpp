
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
//递归写法
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> res;
        mypostorder(root, res);
        return res;
    }

    //后序遍历打印，递归实现
    void mypostorder(Node* node ,vector<int> &res){
        if(node == NULL)  //递归终止条件
            return;
        for(auto point:node->children)
            mypostorder(point,res);
        res.push_back(node->val) ;
    }
};

//非递归写法
#include <stack>
struct Command{
    string s; // go print
    Node* node ;
    Command(string s , Node* node ): s(s) , node(node){}
};

class Solution1 {
public:
    vector<int> postorder(Node* root) {
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
                for(int i=command.node->children.size()-1; i>=0; --i){
                    if(command.node->children[i])
                        stack1.push(Command("go", command.node->children[i]));
                }
            }
        }
        return  res ;
    }
};