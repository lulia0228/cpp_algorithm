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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL)
            return NULL;
        int len = 0;
        ListNode* count = head;
        while(count != NULL){
            count = count->next;
            ++len;
        }
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        for(int i=0 ; i < k%len; i++){ //这里使用了循环，一次移动一位；也可以根据k%len的值 把链表切成2段再拼接，详见下面
            ListNode* cur = dummy;
            ListNode* nex = dummy->next;
            while (nex->next != NULL){
                cur = cur->next;
                nex = nex->next;
            }
            cur->next = NULL;
            nex->next = dummy->next;
            dummy->next = nex;
        }
        return dummy->next;
    }

};


class Solution1 {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL)
            return head;
        int len = 1;
        ListNode* tail = head;
        while(tail->next != NULL){
            tail = tail->next;
            ++len;
        }
        if(k%len == 0)
            return head;

        ListNode* last = head;
        for(int i=0 ; i < len-k%len-1; i++)
            last = last->next;

        ListNode* new_start = last->next;
        last->next = NULL;
        tail->next = head;

        return new_start;
    }

};