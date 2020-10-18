
//反转链表

#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//迭代写法，三指针pre cur(head) back
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) return NULL;
        ListNode* pre = NULL;
        ListNode* back = head;
        while(head){
            //先记下当前节点head后面的节点,这里back指的是cur右边， pre是cur的左边
            back = head->next;
            head->next = pre;
            pre = head;
            head = back;
        }
        return pre;
    }
};

//递归写法
class Solution1 {
public:
    ListNode* reverseList(ListNode* head) {
        if( head == NULL ||head->next == NULL)
            return head;
        ListNode* new_head = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return new_head;
    }

};

//标准单元 头插法 但是头插法不是在原链表上操作
class Solution2 {
public:
    ListNode* reverseList(ListNode* head) {
        if( head == NULL ||head->next == NULL)
            return head;
        ListNode* new_head = new ListNode(-1);
        while(head != NULL){
            //标记当前节点的下一个节点
            ListNode* tmp = head->next;
            //当前节点连接头节点后的节点
            head->next = new_head->next;
            //头节点连接当前节点
            new_head->next = head;
            head = tmp;
        }
        return new_head->next;
    }

};