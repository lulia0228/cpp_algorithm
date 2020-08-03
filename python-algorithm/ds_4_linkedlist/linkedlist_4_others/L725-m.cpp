//
// Created by LiHeng on 2020/7/19.
//

#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        vector<ListNode*> res(k, NULL);
        int len = 0;
        ListNode* cnt = root;
        while(cnt){
            ++len;
            cnt = cnt->next;
        }
        int size = len/k;
        int mod = len%k;
        ListNode* start = root;
        ListNode* cur = root;
        //下面的设计比较巧妙，自己没想到
        for (int i = 0; cur != NULL && i < k; i++) {
            res[i] = cur;
            int curSize = size + (mod-- > 0 ? 1 : 0);
            for (int j = 0; j < curSize - 1; j++) {
                cur = cur->next;
            }
            ListNode* next = cur->next;
            cur->next = NULL;
            cur = next;
        }
        return res;
    }

};