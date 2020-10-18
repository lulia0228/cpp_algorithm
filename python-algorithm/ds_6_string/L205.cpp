
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

//2 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

class Solution1 {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> preIndexOfS(256,0);
        vector<int> preIndexOfT(256,0);
        for (int i = 0; i < s.size(); i++) {
            if (preIndexOfS[s[i]] != preIndexOfT[t[i]]) {
                return false;
            }
            preIndexOfS[s[i]] = i;
            preIndexOfT[t[i]] = i;
        }
        return true;
    }
};

