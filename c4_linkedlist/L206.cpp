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
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *pre = NULL ;
        ListNode *next = NULL ;

        while(head != NULL){
            next = head->next ;
            head->next = pre ;
            pre = head ;
            head = next ;
        }
        return pre ;
    }

    //leetcode 206 反转一个单链表
//思路1： 设置2个节点 一前一后
    ListNode* reverseList1(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *pre = NULL ;
        ListNode *next = NULL ;

        while(head != NULL){
            next = head->next ;
            head->next = pre ;
            pre = head ;
            head = next ;
        }
        return pre ;
    }

//思路2： 递归写法
    ListNode* reverseListR(ListNode* head) {
        if(!head||!head->next) return head;
        else{
            ListNode *new_head = reverseListR(head->next);
            head->next->next = head;
            head->next = NULL;
            return new_head;
        }
    }
};


