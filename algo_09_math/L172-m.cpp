//
// Created by LiHeng on 2020/6/30.
//
#include <iostream>

using namespace std;
class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            count += n / 5;
            n = n / 5;
        }
        return count;
    }
};

/*
看一个例子:
原理：判断有多少个2*5 就有多少个0
11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 11 * (2 * 5) * 9 * (4 * 2) * 7 * (3 * 2) * (1 * 5) * (2 * 2) * 3 * (1 * 2) * 1
对于含有 2 的因子的话是 1 * 2, 2 * 2, 3 * 2, 4 * 2 ...
对于含有 5 的因子的话是 1 * 5, 2 * 5...
含有 2 的因子每两个出现一次，含有 5 的因子每 5 个出现一次，所有 2 出现的个数远远多于 5，换言之找到一个 5，一定能找到一个 2 与之配对。所以我们只需要找有多少个 5。
直接的，我们只需要判断每个累乘的数有多少个 5 的因子即可。
class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        for(int i=1; i<=n; i++){
            int num = i;
            while(num){
                if(num%5 == 0){
                    count++;
                    num/=5;
                }
                else
                    break;
            }
        }
        return count;
    }
};
可以发现超时了，所以要想新的办法计算5因子的个数
每隔 5 个数出现一个 5，所以计算出现了多少个 5，我们只需要用 n/5 就可以算出来
每隔 25 个数字，出现的是两个 5，所以除了每隔 5 个数算作一个 5，每隔 25 个数，还需要多算一个 5
....
最终 5 的个数就是 n / 5 + n / 25 + n / 125 ...
太难了，这题，数学问题，想不到啊！！！
*/