//
// Created by LiHeng on 2020/4/28.
//
#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>

using namespace std ;
//1 DFS 递归 做减法
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        dfs("", n, n, res);
        return res;
    }

    void dfs(string cur, int left, int right, vector<string>& res){
        /* @param cur 当前递归得到的结果
        * @param left   左括号还有几个可以使用
        * @param right  右括号还有几个可以使用
        * @param res    结果集*/

        // 因为每一次尝试，都使用新的字符串变量，所以无需回溯
        // 在递归终止的时候，直接把它添加到结果集即可，注意与「力扣」第 46 题、第 39 题区分
        if(left == 0 && right== 0){
            res.push_back(cur);
            return;
        }
        // 剪枝（如图，左括号可以使用的个数严格大于右括号可以使用的个数，才剪枝，注意这个细节
        if(left > right)
            return;
        if(left > 0)
            dfs(cur+'(', left-1, right, res);
        if(right > 0)
            dfs(cur+')', left, right-1, res);
    }
};


//2 DFS 递归 做加法
class Solution1 {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        dfs("", 0, 0, n, res);
        return res;
    }

    void dfs(string cur, int left, int right, int count, vector<string>& res){
        /* @param cur 当前递归得到的结果
        * @param left   左括号已经用了几个
        * @param right  右括号已经用了几个
        * @param count  左括号/右括号一共需要用几个
        * @param res    结果集 */

        if(left == count && right== count){
            res.push_back(cur);
            return;
        }
        if(left < right)
            return;
        if(left < count)
            dfs(cur+'(', left+1, right, count, res);
        if(right < count)
            dfs(cur+')', left, right+1, count, res);
    }
};

//3 BFS 抽象成一个二叉树 借助队列实现广搜
//通过编写广度优先遍历的代码，可以体会一下，为什么搜索几乎都是用深度优先遍历（回溯算法）。
//广度优先遍历，得程序员自己编写结点类或结构体，显式使用队列这个数据结构。深度优先遍历的时候，就可以直接使用系统栈（递归使用系统栈），
//在递归方法执行完成的时候，系统栈顶就把我们所需要的状态信息直接弹出，而无须编写结点类和显示使用栈。当然也可以显式使用栈。

#include <queue>
struct Node {
    string s;
    int left;
    int right;
    Node(string s, int l, int r) : s(s), left(l), right(r) {}
};

class Solution2{
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        queue<Node> q1;
        q1.push(Node("", n, n));
        while(!q1.empty()){
            Node cur_node = q1.front();
            q1.pop();
            if(cur_node.left == 0 && cur_node.right == 0)
                res.push_back(cur_node.s);
            if(cur_node.left > 0)
                q1.push(Node(cur_node.s+'(', cur_node.left-1, cur_node.right));
            if(cur_node.right > 0 && cur_node.left < cur_node.right)
                q1.push(Node(cur_node.s+')', cur_node.left, cur_node.right-1));
        }
        return res;
    }
};


// 4 借助显式栈 实现深搜
// 注意：把queue换成stack 就变成DFS了  后面研究下二者结果的排布，发现刚好是倒过来了 需要弄清楚运行过程
#include <stack>
class Solution3{
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        stack<Node> q1;
        q1.push(Node("", n, n));
        while(!q1.empty()){
            Node cur_node = q1.top();
            q1.pop();
            if(cur_node.left == 0 && cur_node.right == 0)
                res.push_back(cur_node.s);
            if(cur_node.left > 0)
                q1.push(Node(cur_node.s+'(', cur_node.left-1, cur_node.right));
            if(cur_node.right > 0 && cur_node.left < cur_node.right)
                q1.push(Node(cur_node.s+')', cur_node.left, cur_node.right-1));
        }
        return res;
    }
};


// 5 DP法 不容易想明白状态转移方程
// dp[i] = "(" + dp[可能的括号对数] + ")" + dp[剩下的括号对数]
// dp[i] = "(" + dp[j] + ")" + dp[i- j - 1] , j = 0, 1, ..., i - 1
class Solution4 {
public:
    vector<string> generateParenthesis(int n) {
        if (n == 0) return {};
        if (n == 1) return { "()" };
        vector<vector<string>> dp(n+1);
        dp[0] = { "" };
        dp[1] = { "()" };
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <i; j++) {
                for (string p : dp[j])
                    for (string q : dp[i - j - 1]) {
                        string str = "(" + p + ")" + q;
                        dp[i].push_back(str);
                    }
            }
        }
        return dp[n];
    }
};

//以上5种做法还是DP最快


//1.1 递归：DFS
class Solution6 {
public:
    vector<string> res;
    vector<string> generateParenthesis(int n) {
        string ss;
        _generate(0, 0, n, ss);
        return res;
    }
    //lt rt 代表已经使用的左右括号个数
    void _generate(int lt, int rt, int n, string s){
        if(lt==n && rt==n){
            res.push_back(s);
            return;
        }
        if(lt < n) //已经使用的左括号个数小于n
            _generate(lt+1, rt, n, s+"(");
        if(lt > rt) //左括号个数大于有括号才可以添加右括号
            _generate(lt, rt+1, n, s+")");
    }
};

//1.2 递归：DFS
class Solution7 {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        dfs("", n, n, res);
        return res;
    }
    //和1.1反着来，left right表示剩下的可供使用的括号数
    void dfs(string cur, int left, int right, vector<string>& res){
        if(left == 0 && right== 0){
            res.push_back(cur);
            return;
        }
        if(left > right) //剪枝
            return;
        if(left > 0)
            dfs(cur+'(', left-1, right, res);
        if(right > 0)
            dfs(cur+')', left, right-1, res);
    }
};

//2 BFS 设计队列完成（速度会慢下来）
#include <queue>
struct Node {
    string s;
    int left;
    int right;
    Node(string s, int l, int r) : s(s), left(l), right(r) {}
};

class Solution8{
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0)
            return res;
        queue<Node> q1;
        q1.push(Node("", n, n));
        while(!q1.empty()){
            Node cur_node = q1.front();
            q1.pop();
            if(cur_node.left == 0 && cur_node.right == 0)
                res.push_back(cur_node.s);
            if(cur_node.left > 0)
                q1.push(Node(cur_node.s+'(', cur_node.left-1, cur_node.right));
            if(cur_node.right > 0 && cur_node.left < cur_node.right)
                q1.push(Node(cur_node.s+')', cur_node.left, cur_node.right-1));
        }
        return res;
    }
};