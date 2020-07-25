//
// Created by LiHeng on 2020/7/19.
//

#include <iostream>
#include <stack>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//题目要求不能修改原来的链表，所以就没法反转链表采用leetcode 2的做法
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(-1);
        stack<int> stk1 = buildStack(l1);
        stack<int> stk2 = buildStack(l2);
        int carry = 0;
        while(!stk1.empty() || !stk2.empty()){
            int val1 = 0;
            if(!stk1.empty()){
                val1 = stk1.top();
                stk1.pop();
            }
            int val2 = 0;
            if(!stk2.empty()){
                val2 = stk2.top();
                stk2.pop();
            }
            int tmp = val1 + val2 + carry;
            // 相当于不停的在dummy后面插入新的节点
            ListNode* node = new ListNode(tmp%10);
            node->next = dummy->next;
            dummy->next = node;
            carry = tmp/10;
        }
        //处理最后一次进位
        if(carry > 0){
            ListNode* node = new ListNode(1);
            node->next = dummy->next;
            dummy->next = node;
        }
        return dummy->next;
    }

    stack<int> buildStack(ListNode* l){
        stack<int> res;
        while(l != NULL){
            res.push(l->val);
            l = l->next;
        }
        return res;
    }
};