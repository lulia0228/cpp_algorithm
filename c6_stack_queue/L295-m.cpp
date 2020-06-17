//
// Created by LiHeng on 2020/5/22.
//
#include <iostream>
#include <queue>
using namespace std;

class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<int, vector<int>, less<int> > q1; //大顶堆
    priority_queue<int, vector<int>, greater<int> > q2;//小顶堆

    MedianFinder() {}

    void addNum(int num) {
        if(q1.empty() || num <= q1.top())
            q1.push(num);
        else
            q2.push(num);

        if(q1.size() == q2.size()+2){ //左边和右边多2个数，即维持左边比右边多一个数
            q2.push(q1.top());
            q1.pop();
        }
        if(q1.size() == q2.size()-1){ //左边和右边少1个数，即维持左边比右边多一个数
            q1.push(q2.top());
            q2.pop();
        }

        //另一种写法
        //q1.push(num);
        //q2.push(q1.top());
        //q1.pop();
        //if(q1.size() < q2.size()){
            //q1.push(q2.top());
            //q2.pop();
        //}
    }

    double findMedian(){
        return q1.size() == q2.size()? (q1.top()+q2.top())/2.0 : q1.top() ; //必须是除以2.0  不能是除以2   c++除法运算是向下取整
    }

};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */