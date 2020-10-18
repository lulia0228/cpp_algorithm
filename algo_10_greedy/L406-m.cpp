

// 为了使插入操作不影响后续的操作，身高较高的学生应该先做插入操作，否则身高较小的学生原先正确插入
// 的第k个位置可能会变成第k+1个位置。

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<vector<int>> res;
        for(auto &v:people){
            res.insert(res.begin()+v[1], v);
        }
        return res;
    }

    static bool cmp(vector<int>&a, vector<int>&b){
        return a[0]==b[0]? a[1]<b[1]:a[0]>b[0];
    }
};


//python写法
/*

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        print(people)
        output = []
        for p in people:
        output.insert(p[1], p)
        return output

 */