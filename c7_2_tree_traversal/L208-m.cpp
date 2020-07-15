//
// Created by LiHeng on 2020/5/20.
//
#include <iostream>
#include <cstring>
using namespace std;

//设计一个前缀树
class Trie {
private:
    bool isEnd;     //当前字符是不是单词的结尾
    Trie* next[26]; //指针数组

public:
    Trie() {
        isEnd = false;
        memset(next, 0, sizeof(next));//将next所指向的内存中的前sizeof(next)字节初始化为0
    }

    void insert(string word) {
        Trie* node = this;
        for (char c : word) {  //并没有显式的存储字符，而是存在数组索引里
            if (node->next[c-'a'] == NULL) {
                node->next[c-'a'] = new Trie();
            }
            node = node->next[c-'a'];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = this;
        for (char c : word) {
            node = node->next[c - 'a'];
            if (node == NULL) {
                return false;
            }
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* node = this;
        for (char c : prefix) {
            node = node->next[c-'a'];
            if (node == NULL) {
                return false;
            }
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */