//
// Created by liheng on 19-8-27.
//

#include <iostream>
#include <vector>
#include <cassert>
#include <ctime>
using namespace std ;

//归并排序 （递归版本） 非递归版本怎么写

vector<int> merge(vector<int>& a , vector<int>& b){
    vector<int> c ;
    int i = 0 ;
    int j = 0 ;
    while(i < a.size() && j < b.size()){
        if(a[i] < b[j]){
            c.push_back(a[i]);
            i++;
        }
        else {
            c.push_back(b[j]);
            j ++ ;
        }
    }
    if(i == a.size()){
        for(int k = j ; k < b.size() ; k++)
            c.push_back(b[k]);
    }
    else{
        for(int k = i ; k < a.size() ; k++)
            c.push_back(a[k]);
    }
    return c ;
}

vector<int> gb_Sort(vector<int> & nums){
    if(nums.size() <= 1)
        return nums ;
    int middle =  (int)nums.size()/2 ;
    vector<int> left_nums ;
    for(int i = 0 ;i < middle ; i++){
        left_nums.push_back(nums[i]);
    }
    vector<int> right_nums ;
    for(int i = middle ; i < nums.size() ;i++){
        right_nums.push_back(nums[i]);
    }

    vector<int> left_sort = gb_Sort(left_nums);
    vector<int> right_sort = gb_Sort(right_nums);

    return  merge(left_sort , right_sort) ;
}


int main(){
    int b[] = {4,1,7,6,9,2,8,0,3,5};
    vector<int> vec2(b , b+10);
    vector<int> re_vec = gb_Sort(vec2);
    for(int i = 0 ; i < re_vec.size(); i++)
        cout << re_vec[i] << "\t";
    return 0 ;

}
