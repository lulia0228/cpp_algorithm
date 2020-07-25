//
// Created by LiHeng on 2019/8/10.
//

//优先队列 也是队列 优先队列的底层实现是堆
//手写堆的实现
//c++语言中 优先队列对应的容器类是priority_queque 默认情况下是最大堆

#include <iostream>
#include <queue>
#include <functional>
#include <ctime>
using namespace std ;

bool myRuleCompare(int a ,int b){
    return a%10 < b%10 ; //按个位数字比较
}

int main(){
    srand(time(NULL)) ;
    priority_queue<int> pq ;
    for(int i = 0 ; i < 10 ; i++){
        int num  = rand()%100 ;
        pq.push(num) ;
    }
    while(!pq.empty()){
        cout << pq.top() << "\t" ; //从小到大
        pq.pop() ;
    }

    cout << endl <<endl ;
    priority_queue<int , vector<int> , greater<int> > pq2 ; //最小堆
    // greater和less是std实现的两个仿函数（就是使一个类的使用看上去像一个函数。其实现就是类中实现一个operator()，
    // 这个类就有了类似函数的行为，就是一个仿函数类了）

    for(int i = 0 ; i < 10 ; i++){
        int num  = rand()%100 ;
        pq2.push(num) ;
    }
    while(!pq2.empty()){
        cout << pq2.top() << "\t" ; //从小到大
        pq2.pop() ;
    }

    cout << endl <<endl ;
    priority_queue<int , vector<int> , function<bool(int,int)> > pq3(myRuleCompare) ; //自定义比较函数  必须要引入#include <functional>
    for(int i = 0 ; i < 10 ; i++){
        int num  = rand()%100 ;
        pq3.push(num) ;
    }
    while(!pq3.empty()){
        cout << pq3.top() << "\t" ; //根据个位数来比较
        pq3.pop() ;
    }

}

