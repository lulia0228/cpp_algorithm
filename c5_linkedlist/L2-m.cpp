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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {    //加法十进制向后进位
        ListNode* head = new ListNode(-1);   //存放结果的链表
        ListNode* h = head;//移动指针
        int sum = 0;//每个位的加和结果
        bool carry = false;//进位标志
        while(l1 != NULL || l2 != NULL) //采用||处理后，只要有一个没走到结尾就不会退出循环，
             // 已经走到结尾的在循环体内部再做处理，这样就不需要处理数字位数不一样而在短的后面补0
        {
            sum = 0;
            if(l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;
            }
            if(carry) //是否加1判定;依据上一步是否进位的判定标志carry
                sum++;
            h->next = new ListNode(sum%10);//创建新节点
            h = h->next;
            carry = sum>=10 ? true:false;
        }
        if(carry)
            h->next = new ListNode(1); //处理最高位进1
        return head->next;
    }
};