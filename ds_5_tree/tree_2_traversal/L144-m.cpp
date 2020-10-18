
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode{
    int val ;
    TreeNode* left ;
    TreeNode* right ;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};

//1 递归写法
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder(root, res);
        return res;
    }

    //前序遍历打印，递归实现
    void preorder(TreeNode* node , vector<int> &res){
        if(node == NULL)  //递归终止条件
            return;
        res.push_back(node->val) ;
        preorder(node->left , res);
        preorder(node->right,res);
    }
};


//2 非递归写法
#include <stack>
class Solution1 {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty()){
            TreeNode* cur = s.top();
            s.pop();
            if(cur == NULL) continue;
            res.push_back(cur->val);
            //if(cur->right != NULL )
            s.push(cur->right); //注意是cur->right 不是root->right这是容易犯的低级笔误
            //if(cur->left != NULL )
            s.push(cur->left);
        }
        return res;
    }

};

//前序遍历，这样写也可以的
class Solution2 {
public:
    vector<int> preorderTraversal(TreeNode* root){
        vector<int> res;
        if(root == nullptr) return res;
        stack<TreeNode*> stack;
        while (!stack.empty() || root != nullptr) {
            while (root != nullptr) {
                stack.push(root);
                res.push_back(root->val);
                root = root -> left;
            }
            root = stack.top();
            stack.pop();
            root = root -> right;
        }
        return res;
    }
};

//3 栈迭代，二叉树前中后三种遍历的统一写法

// Command数据结构可以用pair<TreeNode*, string>代替
struct Command{
    string s; // go  print
    TreeNode* node ;
    Command(string s, TreeNode* node ): s(s) , node(node){}
};

class Solution3 {
public:
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
            else{ //进栈操作，注意3个的顺序
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

    vector<int> res = Solution2().preorderTraversal(root);
    for(auto i:res)
            cout << i << "\t";

    return 0;
}

//  2	1	6	3	4	0
//                   2
//                 /   \
//                1     3
//                 \   /
//                  6 4
//                     \
//                      0