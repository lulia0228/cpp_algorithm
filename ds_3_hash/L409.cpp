
#include <iostream>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int longestPalindrome(string s) {
        int res = 0 ;
        int flag = 0;
        unordered_map<char,int> m;
        for(auto c:s)
            m[c]++;
        for(auto p:m){
            if(p.second%2 == 0)
                res += p.second;
            else{
                res += p.second-1;
                flag = 1;
            }
        }
        return flag == 0? res:res+1;
    }
};