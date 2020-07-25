//
// Created by LiHeng on 2020/6/3.
//
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int helper(int left,int right,string s,unordered_map<char,int> count,int k)
    {
        int ans = 0;
        while(right-left>=k-1)
        {
            unordered_map<char,int>::iterator itr = count.begin();
            while(itr!=count.end()) // This loop is to check whether all characters in this window are at least k
            {
                if(itr->second<k and itr->second!=0)  //itr->second!=0这个条件不能去掉，代表的是当前窗口中没有出现该字符
                    break;
                itr++;
            }
            if(itr==count.end()) // if all characters are atleast k
                return max(ans,right-left+1);
            count[s[left]]--; //Since reducing the window size so reduce the frequency of that character
            left++;// reduce the window size
        }
        return ans;
    }

    int longestSubstring(string s, int k)
    {
        unordered_map<char,int> count;
        int res = 0;
        for(int i=0;i<s.size();i++)
        {
            count[s[i]]++;
            if(i>=k-1 and count[s[i]]>=k) // call the helper only when the window size is atleast k and count of the current character is atleast k
                res = max(res,helper(0,i,s,count,k));
        }
        return res;
    }
};

//L340  至多包含 K 个不同字符的最长子串  锁  可以参考L395解法