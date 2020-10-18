
#include <iostream>
#include <vector>
#include <map>

using namespace std;
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        //不能用unordered_map因为要保证有序
        map<int,string> mp;
        mp.insert(make_pair(3, "Fizz"));
        mp.insert(make_pair(5, "Buzz"));
        //mp.insert(make_pair(7, "Jazz"));
        for(int num=1; num<=n; ++num){
            string tem_str = "";
            for(auto k:mp)
                if((num%k.first) == 0)
                    tem_str += k.second;
            if(tem_str == "")
                tem_str+=to_string(num);
            res.push_back(tem_str);
        }
        return res;
    }
};

//这道题写这么麻烦，用到了哈希表，主要是为了通用性，如果游戏扩大：
//能被7整除只需要加上一行 mp.insert(make_pair(7, "Jazz")) ,比手动写条件判断可轻松多了