
#include <iostream>
using namespace std;

//对于每个节点而言，四种路径情况:
// 1 路径只包含节点本身；
// 2 路径只包含左子树+本身；
// 3 路径只包含本身+右子树；
// 4 路径包含左子树+本身+右子树

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//新建立函数 int max_sum(TreeNode* p, int &ans)用以计算自底向上到结点p(必须包含p)为止能得到的最大连续和。
//然后将ans与p->val max_left+p->val max_right+p->val max_left+max_right+p->val进行比较，获取最大值。

// 后序遍历
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        // if(root = NULL) return 0;
        int ans = root->val; //ans的初始值必须要树中某一个节点的值
        max_sum(root, ans);
        return ans;
    }

    // 自底向上到结点p(包含)为止能得到的最大连续和是ans;
    int max_sum(TreeNode* p, int &ans){
        if(p == NULL)
            return 0;
        int max_left = max_sum(p->left, ans);  // 左子树到left node(包含)为止能得到的最大单程sum
        int max_right = max_sum(p->right, ans);  // 右子树到right node(包含)为止能得到的最大单程sum

        // 判断最大ans ：
        // ans
        // max_left  max_right  -- 计算max_sum(left)/max_sum(right)时已计算
        // p->val
        // max_left+p->val  max_right+p->val
        // max_left+max_right+p->val
        ans = max(ans, p->val);
        ans = max(ans, max_left+p->val);
        ans = max(ans, max_right+p->val);
        ans = max(ans, max_left+max_right+p->val);
        // cout << "node: " << p->val << " max_left: " << max_left << " max_right: " << max_right << " ans: " << ans << endl;

        if(max_left <= 0 && max_right <= 0)
            return p->val;
        else
            return (max_left>max_right)?(max_left+p->val):(max_right+p->val);
    }
};

