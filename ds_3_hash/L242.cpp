
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> record(26,0);
        for(int i=0; i<s.size(); ++i)
            record[s[i]-'a']++;
        for(int i=0; i<t.size(); ++i)
            record[t[i]-'a']--;
        for(int i=0; i< record.size(); ++i){
            if(record[i] != 0)
                return false;
        }
        return true;
    }
};
// 能用数组代替表达的时候选数组，效率高过哈希表
// 还有一种方法比较22个字母排序完的结果是否一样