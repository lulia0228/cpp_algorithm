

// 无重复字符最长子串，遍历，以当前元素作为子串结尾

#include <iostream>
#include <cstring>
#include <vector>
using namespace std ;

//方法1
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0)
            return 0;
        int start = 0;
        int max_len = 1;
        for(int i=1 ; i < s.size(); ++i){
            for(int j=start ; j < i; ++j){
                if (s[j] == s[i]){
                    start = j+1;
                    break;
                }
            }
            max_len = max(max_len, i-start+1);
        }
        return max_len;
    }
};

//方法2 同样是滑动窗口；更加模板化
#include <unordered_map>
class Solution1 {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> window;

        int left = 0, right = 0;
        int res = 0; // 记录结果
        while (right < s.size()) {
            char c = s[right];
            right++;
            // 进行窗口内数据的一系列更新
            window[c]++;
            // 判断左侧窗口是否要收缩
            while (window[c] > 1) {
                char d = s[left];
                left++;
                // 进行窗口内数据的一系列更新
                window[d]--;
            }
            // 在这里更新答案
            res = max(res, right - left);
        }
        return res;
    }
};

//方法3
class Solution2 {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        //int hash[256] = {-1};//误区:花括号中只有为0才是全部初始化为0;否则首元素初始化为指定的值,其余的还是0
        vector<int> hash(256,-1); //这才是全部初始化为-1
        if(size == 0)
            return 0;
        int start = 0, maxL = 1 ;
        for(int end=0 ; end < size ;end++){
            if(hash[s[end]] >= start){ //s[end]已经出现过,且一定要大于start,才能更新start
                start = hash[s[end]] + 1 ; //不能使用hash[s[end]]++  因为这样会修改了原来hash[s[end]]对应的值
                maxL = max(maxL,end-start+1);
                hash[s[end]] = end;
            }
            else{//s[end]没有出现过
                maxL = max(maxL,end-start+1);
                hash[s[end]] = end;
            }
        }
        return maxL;
    }
};

class Solution3{
public:
    int lengthofLongestSubstring(string s){
        int freq[256] = {0};
        int l = 0, r = -1;
        int res = 0;
        while (l < s.size()){
            if (r+1 < s.size() && freq[s[r+1]] == 0){
                r++;
                freq[s[r]]++;
            }
            else{
                freq[s[l]]--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};

int main(){
    string str = "abcabcbb";
    Solution sample = Solution();
    int p = sample.lengthOfLongestSubstring(str);
    cout << p;
}

