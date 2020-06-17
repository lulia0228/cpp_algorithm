//
// Created by LiHeng on 2019/7/28.
//

//双指针技术在链表中的应用
//leetcode  19 删除倒数第n个节点
#include <iostream>
#include <cassert>

using  namespace std ;

struct ListNode{
    int val ;
    ListNode* next ;
    ListNode(int x ): val(x) , next(NULL) {}
};

//同样设置了虚拟头节点
class Solution{
public:
    ListNode* removeNthFromEnd(ListNode* head , int n){
        ListNode* dummyHead = new ListNode(0) ;
        dummyHead->next = head ;
        ListNode* p = dummyHead ;
        ListNode* q = dummyHead ;
        for(int i = 0 ;i < n+1 ; i++){
            assert(q) ;
            q = q->next ;
        }
        while (q!= NULL){
            p = p->next ;
            q = q->next ;
        }
        ListNode* delNode = p->next ;
        p->next = delNode->next ;
        delete delNode ;

        ListNode* retHead = dummyHead->next ;
        delete dummyHead ;
        return retHead;
    }
};

//貌似设置虚拟头节点，速度更快
class Solution1 {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* back = dummy;
        ListNode* front = dummy;
        for(int i=0; i<n; ++i)
            front = front->next;
        while(front->next != NULL){
            back= back->next;
            front = front->next;
        }
        back->next = back->next->next;
        return dummy->next;
    }
};

int main(){

    return  0 ;
}

//练习 leetcode 61 143 234