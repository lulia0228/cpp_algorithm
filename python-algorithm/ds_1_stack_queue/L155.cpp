
#include <iostream>
#include <stack>

using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s1;
    stack<int> s2;
    MinStack() {}

    void push(int x) {
        s1.push(x);
        if(s2.empty())
            s2.push(x);
        else{
            if(x < s2.top())
                s2.push(x);
            else
                s2.push(s2.top());
        }
    }

    void pop() {
        if(!s1.empty()){
            s1.pop();
            s2.pop();
        }
    }

    int top() {
        if(!s1.empty())
            return s1.top();
        throw ;
    }

    int getMin() {
        if(!s2.empty())
            return s2.top();
        throw ;
    }

};


//下面是节省内存的写法，即辅助栈不用存每步对应的最小值

class MinStack2 {
public:
    /** initialize your data structure here. */
    stack<int> s1;
    stack<int> s2;
    MinStack() {

    }

    void push(int x) {
        s1.push(x);
        if(s2.empty() || x <= s2.top() )
            s2.push(x);
    }

    void pop() {
        if(!s1.empty()){
            if(s1.top() == s2.top())
                s2.pop();
            s1.pop();
        }

    }

    int top() {
        if(!s1.empty())
            return s1.top();
        throw ;
    }

    int getMin() {
        if(!s2.empty())
            return s2.top();
        throw ;
    }
};


/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

int main(){
    return 0;
}