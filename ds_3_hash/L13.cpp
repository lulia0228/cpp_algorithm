
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;
class Solution {
public:
    int romanToInt(string s) {
        int result=0;
        unordered_map<char,int> luomab={
                {'I',1},
                {'V',5},
                {'X',10},
                {'L',50},
                {'C',100},
                {'D', 500},
                {'M', 1000}
        };  //初始化哈希表
        for(int i=0;i<s.length();i++)
        {
            if(luomab[s[i]] < luomab[s[i+1]])
                result -= luomab[s[i]];
            else
                result += luomab[s[i]];
        }
        return result;
    }
};

//比上面速度慢多了
class Solution1 {
public:
    int romanToInt(string s) {
        unordered_map<string, int> m = {
                {"I", 1},
                {"IV", 3}, {"IX", 8},
                {"V", 5},
                {"X", 10},
                {"XL", 30}, {"XC", 80},
                {"L", 50},
                {"C", 100},
                {"CD", 300}, {"CM", 800},
                {"D", 500},
                {"M", 1000}
        };

        int r = m[s.substr(0, 1)];
        for(int i=1; i<s.size(); ++i){
            string two = s.substr(i-1, 2);
            string one = s.substr(i, 1);
            r += m[two] ? m[two] : m[one];
        }
        return r;
    }
};

int main(){
    string s1 = "LVIII";
    string s2 = "MCMXCIV";
    cout << Solution().romanToInt(s1)<<endl;
    cout << Solution().romanToInt(s2)<<endl;
}