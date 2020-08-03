//
// Created by LiHeng on 2020/4/23.
//

//两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。


/*
设至少有一种任务A出现次数最多，最大出现次数记为cnt_max（某个任务出现次数的最大值）
设出现次数与cnt_max相等的其它任务有equal_cnt_max个（即同时出现最大次数任务个数-1），1代表的是A
1、有cnt_max个A任务，共有（cnt_max-1）个间隔，每个间隔题目要求插入n个不同的任务，凑不够n个不同任务我们用“待命”来填充。
2、最后一个A后面可能还有其他任务，此时的其他任务只能是出现次数等于cnt_max的任务，不然它早就全部用来填充（（cnt_max-1））
   个间隔了(每个间隔需填充一个，不能填充大于1个是因为本身间隔就已经小于n)
3、特殊情况是n=0，则题目求出来的答案应该是任务的总数，即代码中的task.size();
4、答案要包括任务A的个数，所以答案 ans = max((cnt_max-1)*n + cnt_max + equal_cnt_max,tasks.size())
*/


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int>cnt(26,0);
        for(auto type : tasks)  // 桶排序思想
            cnt[type-'A']++;
        int cnt_max = 0, equal_cnt_max = -1;  // equal_cnt_max初值为-1是因为后面的循环会多算一次，会把A任务算进去
        for(auto i: cnt) cnt_max = max(i, cnt_max);
        for(int i = 25; i>=0; --i)
            if(cnt_max == cnt[i])
                ++equal_cnt_max;  // 统计出现次数与最大出现次数相同的任务总个数
        int ans = max((cnt_max-1)*n+cnt_max+equal_cnt_max, (int)tasks.size()); //特殊情况是n=0,所以需要加这句话，也可以把n=0放到前面单独考虑
        return ans;
    }
};

