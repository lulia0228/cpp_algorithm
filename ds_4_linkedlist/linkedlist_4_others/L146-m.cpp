

// L146 LRU缓存设计

#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

class MyListNode {
public:
    int key;
    int val;
    MyListNode *pre;
    MyListNode *nxt;
    MyListNode(int k, int v) {
        key = k;
        val = v;
        pre = nullptr;
        nxt = nullptr;
    }
};

class LRUCache {
public:
    MyListNode *head;
    MyListNode *tail;
    unordered_map<int, MyListNode *> m;
    int cap;
    int now_size;

    LRUCache(int capacity) {
        now_size = 0;
        cap = capacity;
        head = new MyListNode(-1, -1);
        tail = new MyListNode(-1, -1);
        head->nxt = tail;
        tail->pre = head;
    }

    void lift_now_to_head(MyListNode *now) {
        if (now->pre != nullptr && now->nxt != nullptr) {
            now->pre->nxt = now->nxt;
            now->nxt->pre = now->pre;
        }
        now->nxt = head->nxt;
        now->pre = head;
        head->nxt->pre = now;
        head->nxt = now;
    }

    int get(int key) {
        if (m.find(key) == m.end())
            return -1;
        MyListNode *now = m[key];
        lift_now_to_head(now);
        return now->val;
    }

    void put(int key, int value) {
        MyListNode *now;
        if (m.find(key) == m.end()) {
            now = new MyListNode(key, value);
            if (now_size < cap) {
                now_size++;
                m[key] = now;
            }
            else {
                MyListNode *last = tail->pre;
                last->pre->nxt = tail;
                tail->pre = last->pre;
                m.erase(last->key);
                delete last;
                m[key] = now;
            }
        }
        else {
            now = m[key];
            now->val = value;
        }
        lift_now_to_head(now);
    }
};

#include <list>
class LRUCache1 {
private:
    unordered_map<int,list<pair<int,int>>::iterator> m;//用一个哈希双向链表来存储
    int cap;//表示容量
    list<pair<int,int>> l;//表示双向链表

public:
    //成员函数名称个类名保持一致
    LRUCache1(int capacity) {
        this->cap = capacity;
    }

    int get(int key) {
        //查找缓存中是否存在key。
        auto iter = m.find(key);
        if(iter==m.end()){
            //不存在，就返回--1
            return -1;
        }
        //存在，返回对应的val.并且把该缓存放到最前面。
        int val = iter->second->second;//iter是一个迭代器，iter->second也是一个迭代器。
        put(key, val);
        return val;

    }

    void put(int key, int value) {
        //查找要放入的数是否已经存在。
        auto iter = m.find(key);
        if(iter!=m.end()){
            //若存在。就把链表中原来的数据删除。并把当前数据插入链表头
            l.erase(iter->second);
        }
        //这两步是公共操作。
        l.push_front(make_pair(key,value));
        m[key] = l.begin();
        if(l.size()>cap){
            //若缓存满了。就要删除链表最后一个数据。
            int k = l.back().first;//这里l.back()是一个对象。对象用.
            m.erase(k);
            l.pop_back();
        }
    }

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


int main(){
    LRUCache cache = LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << endl;       // 返回  1
    cache.put(3, 3);    // 该操作会使得密钥 2 作废
    cout << cache.get(2) << endl;       // 返回 -1 (未找到)
    cache.put(4, 4);    // 该操作会使得密钥 1 作废
    cout << cache.get(1) << endl;       // 返回 -1 (未找到)
    cout << cache.get(3) << endl;       // 返回  3
    cout << cache.get(4) << endl;       // 返回  4
}
