//
// Created by 李恒 on 2020/6/30.
//

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        stack<int> stk;
        int sz = digits.size();
        int flag = 1;
        for(int i=sz-1; i>=0; --i){
            int m = (digits[i]+flag)%10;
            flag = (digits[i]+flag)/10;
            stk.push(m);
        }
        if(flag == 1)
            stk.push(1);
        vector<int> res;
        while(!stk.empty()){
            res.push_back(stk.top());
            stk.pop();
        }
        return res;
    }
};