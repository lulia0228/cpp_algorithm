

//部分反转链表

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* start = dummy;
        for(int i=1 ;i<m;i++)
            start = start->next;
        //start是反转位置m的上一个节点
        ListNode* pre = NULL;
        ListNode* tem = start->next; //标记反转位置m
        ListNode* cur = start->next;
        ListNode* back = cur;
        int count = m;
        while(count <= n){
            count++;
            //先记下当前节点cur后面的节点,这里back指的是cur右边， pre是cur的左边
            back = cur->next;
            cur->next = pre;
            pre = cur;
            cur = back;
        }
        //上面循环完之后cur指向反转位置n的下一位;下面连接链表
        start->next = pre;
        tem->next = back;

        ListNode* re = dummy->next;
        delete dummy;
        return re;
    }
};