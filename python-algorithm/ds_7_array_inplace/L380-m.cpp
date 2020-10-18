
//380. 常数时间插入、删除和获取随机元素

// 哈希表+动态数组
//动态数组存储元素值
//哈希表存储存储值到索引的映射。

//因为哈希表只能做到查找插入和查找删除是o(1)； 第三个要求随机返回做不到o(1) 所以需要设计一个
//动态数组用于随机返回，此外删除的时候，动态数组可以把最后一个数字和要删除的数字交换位置，然后数组删除最后一个数，并更新哈希

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class RandomizedSet {
public:
    /** Initialize your data structure here. */
    vector<int> vec;
    unordered_map<int, int> up1;
    RandomizedSet() {}

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(up1.find(val) != up1.end() )
            return false;
        up1.insert(make_pair(val, vec.size()));
        vec.push_back(val);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(up1.find(val) == up1.end())
            return false;
        vec[up1[val]] = vec.back();
        up1[vec.back()] = up1[val]; //把要删除的元素移动到最末尾
        vec.pop_back();
        up1.erase(val);
        return true;

    }

    /** Get a random element from the set. */
    int getRandom() {
        int sz = vec.size();
        if(sz == 0) return 0;
        int index = rand()%sz;
        return vec[index];

    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */