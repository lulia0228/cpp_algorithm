//
// Created by LiHeng on 2020/6/3.
//

//思想：每次出现第三颗新类型的树的时候，更新窗口左边界以及集合中树的类型

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;
class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int lt = 0;
        int len = 1;
        unordered_set<int> st;
        for(int rt=0; rt<tree.size(); ++rt){
            st.insert(tree[rt]);
            if(st.size() == 3){
                lt = rt-2;
                while(tree[lt] == tree[rt-1])
                    --lt;
                st.erase(tree[lt]);
                ++lt;
            }
            else
                len = max(len, rt-lt+1);
        }
        return len;
    }

};
