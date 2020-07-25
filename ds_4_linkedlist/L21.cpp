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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL)
            return l2 ;
        if(l2 == NULL)
            return l1;
        ListNode * re = new ListNode(-1) ;
        ListNode * tem = re ;
        while (l1 != NULL && l2 != NULL){
            if(l1->val <  l2->val){
                tem->next = l1 ;
                l1 = l1->next ;
            }
            else{
                tem->next = l2 ;
                l2 = l2->next ;
            }
            tem = tem->next ;
        }
        tem->next = l1 != NULL ? l1 : l2;
        return re->next ;
    }
};


//递归解法，不太好理解
class Solution1 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 ==NULL) return l2 ;
        if(l2 == NULL) return l1;
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