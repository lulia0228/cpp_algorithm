//
// Created by LiHeng on 2020/7/19.
//
#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//非递归写法，设置一个标记上一次重复值第一次出现的节点
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        ListNode* start = head;
        ListNode* pre = head;//标记上个相同值
        ListNode* cur = head->next;
        while(cur){
            if(cur->val != pre->val){
                pre->next = cur;
                pre = cur;
            }
            cur = cur->next;
        }
        pre->next = NULL;
        return start;
    }
};

//递归写法，有点不好理解
class Solution1 {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        head->next = deleteDuplicates(head->next);
        //cout <<head->val<< head->next->val<<endl;
        //return的东西就是上层递归的返回
        return head->val == head->next->val ? head->next : head;
    }
};