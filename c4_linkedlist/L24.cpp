//
// Created by liheng on 19-8-5.
//

//leetcode 24 交换链表节点

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution{
public:
    ListNode* swapElements(ListNode* head ){
        ListNode* dummyHead = new ListNode(0) ;
        dummyHead-> next = head ;
        ListNode* p = dummyHead ;
        while(p->next && p->next->next){
            ListNode* node1 =  p->next ;
            ListNode* node2 = node1->next ;
            ListNode* next = node2->next ;

            node2->next = node1 ;
            node1->next = next ;
            p->next = node2 ;

            p = node1 ;
        }

        ListNode* retNode = dummyHead->next ;
        delete dummyHead ;

        return retNode ;
    }
};


int main(){

    return 0 ;
}

//练习leetcode 25 147(链表插入排序) 148（对链表排序）