
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> record(26, 0);
        for(int i=0; i<s.size(); ++i)
            record[s[i]-'a']++;
        for(int i=0; i<s.size(); ++i)
            if(record[s[i]-'a'] == 1)
                return i;
        return -1;
    }
};