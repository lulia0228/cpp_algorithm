//
// Created by 李恒 on 2020/7/17.
//
#include <iostream>
using namespace std;

class MapSum {

private:
    bool isEnd;
    MapSum* next[26];
    int val;

public:
    /** Initialize your data structure here. */
    MapSum() {
        isEnd = false;
        memset(next, 0, sizeof(next));
        val = 0;
    }

    void insert(string key, int val) {
        MapSum* node = this;
        for(auto c : key){
            if(node->next[c-'a'] == nullptr) node->next[c-'a'] = new MapSum();
            node = node->next[c-'a'];
        }
        node->isEnd = true;
        node->val = val;
    }

    //从前缀结束处开始搜索目标
    int total(MapSum* root) {
        int res = root->val;
        for(auto node : root->next){
            if(node != nullptr) res += total(node);
        }
        return res;
    }

    //查询是否存在前缀
    int sum(string prefix) {
        MapSum* node = this;
        for(auto c : prefix){
            node = node->next[c-'a'];
            if(node == nullptr) return 0;
        }
        return total(node);
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */


//使用c++ 字符串查找 内置函数find的方法
class MapSum1 {
public:
    map<string,int> mp;
    /** Initialize your data structure here. */
    MapSum() {

    }

    void insert(string key, int val) {
        mp[key] = val;
    }

    int sum(string prefix) {
        int ans = 0;
        string s;
        for(auto it=mp.begin();it!=mp.end();it++){
            s = it->first;
            if(s.find(prefix) == 0){
                ans += (it->second);
            }
        }
        return ans;
    }
};