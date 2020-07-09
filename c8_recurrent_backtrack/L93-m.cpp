//
// Created by 李恒 on 2020/7/9.
//
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;
//对于此类问题，要搞明白每层循环的候选对象到底是什么！！！
class Solution {
public:
    vector<string> res;
    vector<string> restoreIpAddresses(string s) {
        if(s.size()<4)
            return res;
        vector<string> cur;
        dfs(s, 0, 0, cur);
        return res;
    }

    //用count标记下探的层数
    void dfs(string s, int idx, int count, vector<string> & cur){
        if(count == 4 ){
            if(idx == s.size()){
                string t_s = cur[0];
                for(int i=1; i<4; ++i)
                    t_s += "."+cur[i];
                res.push_back(t_s);
            }
            return;
        }
        for(int i=idx,j=0; j<3&&i+j<s.size(); ++j){
            if(stoi(s.substr(i,j+1)) <= 255 && condition1(s.substr(i,j+1))){
                cur.push_back(s.substr(i,j+1));
                dfs(s, i+j+1, count+1, cur);
                cur.pop_back();
            }
        }
    }

    //解决大于255的情况,可以直接调用c++ 自带的stoi
    int str2num(string s){
        int num = 0;
        for(auto c:s){
            num = num*10 + (c-'0');
        }
        return num;
    }

    //解决分成01 010 之类的情况
    bool condition1(string s){
        if (s.size()>1 && s[0] == '0')
            return false;
        return true;
    }

};

int main(){
    string s1 = "25525511135";
    vector<string> res = Solution().restoreIpAddresses(s1);
    for(auto item:res)
        cout << item <<endl;
}