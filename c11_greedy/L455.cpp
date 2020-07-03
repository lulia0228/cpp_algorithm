//
// Created by 李恒 on 2020/7/3.
//

#include <iostream>
#include <vector>
using namespace std;

//s是饼干 g是愿望
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end() , greater<int> ()) ; //默认从小到大，加greater从大到小
        sort(s.begin(), s.end() , greater<int> ()) ; //默认从小到大，加greater从大到小
        int gi = 0 , si = 0;
        int res = 0 ;
        while(gi < g.size() && si < s.size()){
            if(g[gi] <= s[si]){
                res++;
                gi++;
                si++;
            }
            else
                gi++; //gi小孩愿望失败
        }
        return res ;
    }
};