//
// Created by liheng on 19-8-5.
//

//leetcode 237

// 给定链表中的一个节点，将其删除；和前面的区别在于不是给出一个具体的值。只是给出节点

// 解决办法。将当前节点的下一个节点的值覆盖给定的节点，将下一个节点从链表中删除


#include <iostream>
using namespace std ;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* tem = node->next;
        node->val = node->next->val;
        node->next = node->next->next;
        delete tem;
    }
};

class Solution1{
public:
    void deleteNode(ListNode* node ){

        if (node == NULL)
            return;

        //尾节点处理
        if (node->next = NULL){
            delete node ;
            node = NULL ;
            return;
        }

        node->val = node->next->val ;
        ListNode* delNode = node->next ;
        node->next = delNode->next ;
        delete delNode ;

        return;
    }
};


int main(){

    return 0 ;
}

//练习题 leetcode 19