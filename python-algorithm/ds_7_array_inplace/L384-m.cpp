//
// Created by LiHeng on 2020/6/28.
//
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> ori;
    vector<int> coy;
    Solution(vector<int>& nums) {
        ori = nums;
        coy = nums;
    }

    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return coy;
    }

    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for(int i=0; i<ori.size(); ++i)
            my_swap(ori[i], ori[rand()%(ori.size()-i)+i]);
        return ori;
    }

    void my_swap(int& m , int& n){
        int tmp = m;
        m = n;
        n = tmp;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */