

//leetcode 454 4sum

#include <iostream>
#include <unordered_map>
#include <cassert>
#include <vector>

using namespace std;
class Solution1{
public:
    int fourSumCount(vector<int>& A , vector<int>& B, vector<int>& C, vector<int>& D){
        unordered_map<int , int> record ;
        for(int  i = 0 ; i < A.size() ; i++)
            for(int j = 0 ; j < B.size() ; j++)
                record[A[i]+B[j]] ++ ;
        int res = 0 ;
        for(int  i = 0 ; i < C.size() ; i++)
            for(int j = 0 ; j < D.size() ; j++)
                if(record.find(0 - C[i] - D[j]) != record.end())
                    res ++ ;
        return res;
    }
};

//练习题 leetcode 49



//leetcode 447(查找点)
class Solution2{
public:
    int numberOfBoomeranges(vector<pair<int, int>>& points){
        int res = 0 ;
        for(int i = 0 ; i < points.size() ; i++){
            unordered_map<int,int> record ; //不能放在外面
            for(int j = 0 ; j < points.size() ; j++)
                if( j != i)
                    record[ dis(points[i], points[j]) ] ++ ;

            for(unordered_map<int,int>::iterator iter = record.begin(); iter != record.end(); iter++)
                if(record[iter->second] >= 2)
                    res += (iter->second)*(iter->second - 1);

        }
        return  res;
    }

private:
    int dis(const pair<int,int> &pa , const pair<int,int> &pb){
        return (pa.first-pb.first)*(pa.first-pb.first) +
               (pa.second-pb.second)*(pa.second-pb.second);
    }
};


//练习题 leetcode  149
