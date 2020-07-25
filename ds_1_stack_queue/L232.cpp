//
// Created by 李恒 on 2020/7/2.
//
#include <iostream>
#include <stack>
using  namespace std;

class MyQueue {
private:
    stack<int> s1;
    stack<int> s2;
public:
    /** Initialize your data structure here. */
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(s1.empty() && s2.empty()) //可以拿掉，题目条件:空队列不会调用pop peek
            throw runtime_error("Queue is empty!") ;
        if(s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop() ;
            }
        }
        int re = s2.top() ;
        s2.pop() ;
        return re ;
    }

    /** Get the front element. */
    int peek() {
        if(s1.empty() && s2.empty()) //可以拿掉，题目条件:空队列不会调用pop peek
            throw runtime_error("Queue is empty!") ;
        if(s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop() ;
            }
        }
        return s2.top() ;
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty()&&s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */