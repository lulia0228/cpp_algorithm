
//692. 前K个高频单词
//这道题要考虑的细节，string要返回序小的，所以入堆的时候，出现频次一样的时候，需要把字母序小的优先放进去
//另外就是自定义堆的比较函数，比较蛋疼

#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cassert>
#include <algorithm>
using namespace std;

struct comp {
    bool operator()(pair<int,string>& a,pair<int,string>& b){
        return a.first==b.first? a.second<b.second:a.first>b.first;
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        //统计每个元素的出现频率
        unordered_map<string , int> freq ;
        for(int i = 0 ;i < words.size() ; i++)
            freq[words[i]]++ ;

        assert(k <= freq.size());

        // 扫描freq，维护当前频率出现最高的前K个元素
        // c++ stl 优先级队列默认对pair类型第一个元素先做对比
        // 这里因为考虑字母序的问题，所以要自己设计比较函数， 数据对（频率,元素），
        // 按照频率排序做成小顶堆，按照子母序做成大顶堆

        //priority_queue<pair<int,string> , vector<pair<int,string>> , greater<pair<int,int>> > pq ;
        priority_queue<pair<int,string> , vector<pair<int,string>> , comp > pq ;
        for(unordered_map<string,int>::iterator iter = freq.begin() ; iter!= freq.end() ; iter++){
            if (pq.size() == k){
                if(iter->second > pq.top().first){
                    pq.pop();
                    pq.push(make_pair(iter->second, iter->first));
                }
                    //必须用else if 是为了防止上面元素入堆后，堆里有频率相同且字母序大的元素存在，导致重复推入
                else if(iter->second == pq.top().first && iter->first < pq.top().second){
                    pq.pop();
                    pq.push(make_pair(iter->second, iter->first));
                }
            }
            else //优先队列未满时
                pq.push(make_pair(iter->second, iter->first));
        }

        vector<string> res ;
        while(!pq.empty()){
            res.push_back(pq.top().second) ;
            pq.pop() ;
        }
        //先出来的是频率小的，字母序大的
        reverse(res.begin(), res.end());
        return res ;
    }

};

int main(){
    vector<string> s1 = {"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"};
    vector<string> res = Solution().topKFrequent(s1, 4);
    for(auto s:res)
        cout << s <<"\t";
    return 0;
}