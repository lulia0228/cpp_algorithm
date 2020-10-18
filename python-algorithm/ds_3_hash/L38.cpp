
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;
class Solution {
public:
    string countAndSay(int n) {
        string res = "1";
        if(n == 1) return res;
        for(int i=2; i<=n; ++i)
            res = nextStr(res);
        return res;
    }

    string nextStr(string s){
        string res = "";
        char tmp = s[0];
        int index = 0;
        int count = 0;
        while(index<s.size()){
            while(s[index] == tmp){
                index++;
                count++;
            }
            res += to_string(count);
            res += tmp;
            tmp = s[index];
            count = 0;
        }
        return res;
    }

};

//比方说 1211 里有 “ 1 个 1 ， 1 个 2 ， 2 个 1 ” ，那么 111221 就是它的下一个数，再下一个就是312211