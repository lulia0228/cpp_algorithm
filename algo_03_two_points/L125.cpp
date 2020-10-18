
#include <iostream>
#include <cstring>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string ss;
        for(char n:s)
            if(n>='0'&&n<='9')
                ss += n;
            else if(n>='a'&& n<='z')
                ss += n;
            else if(n>='A'&& n<='Z')
                ss += n-'A'+'a';

        int i=0, j=ss.size()-1;
        while(i<j){
            if(ss[i] == ss[j]){
                i++;
                j--;
            }
            else
                return false;
        }
        return true;
    }

};