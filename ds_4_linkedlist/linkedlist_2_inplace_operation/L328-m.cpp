//
// Created by LiHeng on 2020/7/19.
//

//基偶链表

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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode* odd = head; //奇数编号节点 1开始
        ListNode* even = head->next;//偶数编号节点 2开始
        ListNode* label = head->next;//标记第一个偶数点
        //链表长度为奇数时候终止条件是even!=NULL;偶数时even->next !=NULL.
        while(even && even->next){
            //特别注意一点even->next 要放在even之后，不能使用while(even->next && even && odd->next)
            //因为如果even是NULL的话，先判断 even->next会越界报错
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = label;
        return head;
    }
};