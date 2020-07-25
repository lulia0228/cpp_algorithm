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
        if(head == NULL || head->next == NULL) return head;
        int len = 0;
        ListNode* cnt = head;
        ListNode* tail = head; //先把尾节点标记下来
        while(cnt){
            ++len;
            tail = cnt;
            cnt = cnt->next;
        }
        if(k%len == 0) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* cur = head;
        for(int i=0; i<(len-k%len); ++i){
            cur = cur->next;
            pre = pre->next;
        }
        dummy->next = cur;
        tail->next = head;
        pre->next = NULL;
        return dummy->next;
    }
};

//也可以下面这么写，思路是一样的
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