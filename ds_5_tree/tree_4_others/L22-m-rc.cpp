//
// Created by LiHeng on 2020/7/4.
//

#include <iostream>
#include <vector>
#include <cstring>

using  namespace std;
//1.1 递归：DFS
class Solution {
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
class Solution1 {
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