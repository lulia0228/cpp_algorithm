
#include <iostream>
using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == NULL ||head->next == NULL)
            return true;
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast->next != NULL && fast->next->next != NULL){
            fast = fast->next->next ;
            slow = slow->next;
        } //循环结束 当链表长度为奇数，slow指向正中间；偶数，slow指向前半段的最后位置

        //部分反转链表，即反转slow指针后面的链表
        ListNode* back = NULL;
        ListNode* cur = slow->next;
        ListNode* front = cur;
        while(front!=NULL){
            front = cur->next;
            cur->next = back;
            back = cur;
            if(front)
                cur = front;
        }
        slow->next = cur; //连接链表

        while(cur!=NULL){
            if(cur->val != head->val )
                return false;
            else{
                cur = cur->next;
                head = head->next;
            }
        }
        return true;
    }
};