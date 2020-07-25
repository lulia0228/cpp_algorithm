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

//设置虚拟头节点
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        //一直约定的是back是右边的，pre是靠左边的
        ListNode* pre = dummy;
        ListNode* back = dummy;
        for(int i=0; i<n; ++i)
            back = back->next;
        while(back->next != NULL){
            pre = pre->next;
            back = back->next;
        }
        pre->next = pre->next->next;
        return dummy->next;
    }
};

int main(){

    return  0 ;
}

//练习 leetcode 61 143 234