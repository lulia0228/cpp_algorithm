//
// Created by 李恒 on 2020/1/8.
//

#include <iostream>
#include <vector>
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == NULL)
            return NULL;
        ListNode* res = lists[0];
        for(int i=1 ; i< lists.size();i++)
            res = merge2Lists(res , lists[i]);
        return res;
    }

    ListNode* merge2Lists(ListNode* pHead1 , ListNode* pHead2 ){
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



//采用的是两两合并链表，借助一个队列，直到队列里面元素只剩1个
#include <queue>
class Solution1 {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0)
            return NULL;
        if(lists.size() == 1)
            return lists[0];
        queue<ListNode*> q1;
        for(int i=0 ;i < lists.size();i++)
            q1.push(lists[i]);
        while(q1.size()>1){
            ListNode* l1 = q1.front();
            q1.pop();
            ListNode* l2 = q1.front();
            q1.pop();
            ListNode* p = merge2Lists(l1,l2);
            q1.push(p);
        }
        return q1.front();
    }

    ListNode* merge2Lists(ListNode* pHead1, ListNode* pHead2){
        if(pHead1 == NULL)
            return pHead2;
        if(pHead2 == NULL)
            return pHead1;
        ListNode* newHead = new ListNode(0);
        ListNode* tem = newHead;
        while(pHead1 && pHead2){
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
        tem->next = pHead1 ? pHead1:pHead2;
        ListNode* res = newHead->next;
        delete newHead;
        return res;
    }

};
