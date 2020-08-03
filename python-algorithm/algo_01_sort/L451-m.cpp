//
// Created by 李恒 on 2020/7/2.
//
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        string res = "";
        unordered_map<char,int> m;
        for(auto c:s)
            ++m[c];
        vector< pair<int,char> > v;
        for(auto p:m)
            v.push_back(make_pair(p.second,p.first));
        sort(v.begin(), v.end());
        for(auto p:v){
            res = string(p.first,p.second) + res;
            //用到了重复生成字符串的函数string(len,char)，不用这个一个个字符加的话就超时
        }
        return res;
    }

};


class Solution1 {
public:
    string frequencySort(string s) {
        unordered_map<char, int> ump;
        for (auto &c:s) {
            ++ump[c];
        }
        vector<pair<char,int>> vec;
        for (auto &m:ump) {
            vec.push_back(m);
        }
        sort(vec.begin(), vec.end(), cmp);
        string ret;
        for (auto &v:vec) {
            ret += string(v.second, v.first); //重复字符生成字符串
        }
        return ret;
    }

    static bool cmp(pair<char, int> &p1, pair<char, int> &p2){
        return p1.second > p2.second;
    }

};

int main(){
    cout << string(2,'c')<<endl;
}