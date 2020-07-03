//
// Created by 李恒 on 2020/7/3.
//
#include <iostream>
#include <cstring>
#include <unordered_map>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> partitionLabels(string S) {
        unordered_map<char,int> m1;
        unordered_map<char,int> m2;
        for(int i=0; i<S.size(); ++i){
            m2[S[i]] = i;
            if(m1.find(S[i]) == m1.end())
                m1[S[i]] = i;
        }
        vector<vector<int>> rg;
        for(auto p:m1){
            rg.push_back(vector<int>{p.second, m2[p.first]});
        }
        sort(rg.begin(), rg.end());
        vector<vector<int>> merge_rg;
        for (int i=0 ; i<rg.size(); ++i){
            if (merge_rg.empty() || rg[i][0] > merge_rg[merge_rg.size()-1][1])
                merge_rg.push_back(rg[i]);
            else
                merge_rg[merge_rg.size()-1][1] = max(rg[i][1], merge_rg[merge_rg.size()-1][1]);
        }
        vector<int> res;
        for(auto &v:merge_rg)
            res.push_back(v[1]-v[0]+1);
        return res;
    }
};

//贪心写法
class Solution1 {
public:
    vector<int> partitionLabels(string S) {
        unordered_map<char,int> m;
        for(int i=0; i<S.size(); ++i)
            m[S[i]] = i;
        int start=0,boarder=0;
        vector<int> res;
        for(int i=0; i<S.size(); ++i){
            //标记局部最靠后的索引位置
            boarder = max(boarder,m[S[i]]);
            if(i==boarder){
                res.push_back(i-start+1);
                start = i+1;
            }
        }
        return res;
    }
};

//python对应写法
/*

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

 */