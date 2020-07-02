//
// Created by LiHeng on 2020/4/19.
//
#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if(pHead1 == NULL)
            return pHead2;
        if(pHead2 == NULL)
            return pHead1;
        ListNode* new_head = new ListNode(0);
        ListNode* tem = new_head;
        while(pHead1 != NULL && pHead2 != NULL){
            if(pHead1->val > pHead2->val){
                tem->next = pHead2;
                pHead2 = pHead2->next;
            }
            else{
                tem->next = pHead1;
                pHead1 = pHead1->next;
            }
            tem = tem->next;
        }
        tem->next = (pHead1 == NULL)? pHead2:pHead1 ;
        ListNode* re = new_head->next ;
        delete new_head;
        return re;
    }
};


//递归解法
class Solution1 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 ==NULL)
            return l2 ;
        if(l2 == NULL)
            return l1;

        ListNode * re = NULL ;

        if(l1->val < l2->val){
            re = l1 ;
            re->next = mergeTwoLists(l1->next , l2);
        }
        else{
            re = l2 ;
            re->next = mergeTwoLists(l1, l2->next);
        }

        return re ;

    }
};