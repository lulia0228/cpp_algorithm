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

//链表排序-----在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。  使用归并排序法
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(head == NULL || head->next == NULL )
            return head;
        //利用快慢指针拆分成2个链表
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* bre = head;
        while(fast != NULL && fast->next !=NULL){
            fast = fast->next->next;
            bre = slow; //断点
            slow = slow->next;
        }

        bre->next = NULL;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        return merge2lists(l1, l2);
    }

    ListNode* merge2lists(ListNode* h1, ListNode* h2){
        if(h1==NULL)
            return h2;
        if(h2==NULL)
            return h1;
        ListNode* new_head = new ListNode(0);
        ListNode* temN = new_head;
        while(h1!=NULL&&h2!=NULL){
            if(h1->val > h2->val){
                temN->next = h2;
                h2 = h2->next;
            }
            else{
                temN->next = h1;
                h1 = h1->next;
            }
            temN = temN->next;
        }
        temN->next = (h1 == NULL)? h2:h1;
        ListNode* res = new_head->next;
        delete new_head;
        return res;
    }

};