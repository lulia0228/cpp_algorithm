//
// Created by LiHeng on 2020/7/19.
//

//138. 复制带随机指针的链表  这道题思路比较奇特 剑指offer也有这道题

#include <iostream>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    Node() {}
    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == NULL)
            return head;
        copyNext(head);
        copyRandom(head);
        return extractCopyList(head);
    }

    //复制下一个指针
    void copyNext(Node* head){
        Node* tem = head;
        while(tem != NULL){
            Node* clone = new Node(tem->val,tem->next,NULL);//创建原链表节点的复制节点，其中包含原链表的下一个节点的信息
            tem->next = clone; //原链表连上复制节点，复制节点上一步创建时已经连上原链表的下一个节点
            tem = clone->next; //跳到原链表的下一个节点
        }
    }

    //复制随机指针
    void copyRandom(Node* head){
        Node* tem = head;
        while(tem != NULL){
            Node* cloned = tem->next;
            if(tem->random != NULL)
                cloned->random = tem->random->next;
            tem = cloned->next;
        }
    }

    //分离奇偶编号链表
    Node* extractCopyList(Node* head){
        Node* tem = head;
        Node* copyListHead = head->next;
        Node* copyNode = copyListHead;
        while(tem != NULL){
            tem->next = tem->next->next;
            if(copyNode->next != NULL)
                copyNode->next = copyNode->next->next;
            tem = tem->next;
            copyNode = copyNode->next;
        }
        return copyListHead;
    }

};