//
// Created by LiHeng on 2020/5/20.
//
//找出数组的中的前K个高频元素，时间复杂多要优于nlogn
//哈希+加优先级队列(stl中底层是堆实现的)

#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <cassert>

using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        assert(k > 0) ;
        //统计每个元素的出现频率
        unordered_map<int , int> freq ;
        for(int i = 0 ;i < nums.size() ; i++)
            freq[nums[i]] ++ ;

        assert(k <= freq.size());

        //扫描freq，维护当前频率出现最高的前K个元素
        //在优先队列中存储为数据对（频率,元素），按照频率排序，做成最小堆，因为每次弹出队列里面频率最小的
        //c++  stl 优先级队列默认对pair类型第一个元素先做对比，这里不想自己写比较函数的话，就把相比较的值放到前面

        priority_queue<pair<int,int> , vector<pair<int,int>> , greater<pair<int,int>> > pq ;
        for(unordered_map<int,int>::iterator iter = freq.begin() ; iter!= freq.end() ; iter++){
            if (pq.size() == k){
                if(iter->second > pq.top().first){
                    pq.pop();
                    pq.push(make_pair(iter->second, iter->first));
                }
            }
            else //优先队列未满时
                pq.push(make_pair(iter->second, iter->first));
        }

        vector<int> res ;
        while(!pq.empty()){
            res.push_back(pq.top().second) ;
            pq.pop() ;
        }
        return res ;
    }
};