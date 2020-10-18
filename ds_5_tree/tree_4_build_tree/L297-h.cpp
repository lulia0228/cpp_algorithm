

// 二叉树的序列化本质上是对其值进行编码，更重要的是对其结构进行编码。
// 可以遍历树来完成上述任务。众所周知，我们一般有两个策略：BFS/DFS。
// BFS 可以按照层次的顺序从上到下遍历所有的节点
// DFS 可以从一个根开始，一直延伸到某个叶，然后回到根，到达另一个分支。
// 根据根节点、左节点和右节点之间的相对顺序，可以进一步将DFS策略区分为：先序遍历 中序遍历后序遍历

#include <iostream>
#include <sstream>
#include <cstring>
using namespace std;

//DFS    用BFS我写失败了Fuck
// * Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(root==NULL)
            return string ();
        stringstream ss;
        dfs(root , ss);
        return ss.str();
    }

    void dfs(TreeNode* rt,stringstream& ss){
        if(rt == NULL){
            ss << "# ";// #后面有空格
            return ;
        }
        ss << rt->val << ' '; // << 向流中传值
        dfs(rt->left , ss);
        dfs(rt->right , ss);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.empty())
            return NULL;
        TreeNode* rt = NULL;
        stringstream ss(data);
        rebuild(rt , ss);
        return rt;
    }

    void rebuild(TreeNode* &rt,stringstream& ss){
        string t;
        ss >> t; // >> 向t中写入值
        if(t[0] == '#'){
            rt = NULL;
            return;
        }
        rt = new TreeNode(stoi(t));
        rebuild(rt->left, ss);
        rebuild(rt->right, ss);
    }

};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

#include <vector>
int main(){
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    TreeNode* layer1_r = root->right;
    layer1_r->left = new TreeNode(4);
    layer1_r->right = new TreeNode(5);
    Codec codec;
    string s = codec.serialize(root);
    cout << s << endl;
    return 0;
}

//         1
//        / \
//       2   3
//          / \
//         4   5