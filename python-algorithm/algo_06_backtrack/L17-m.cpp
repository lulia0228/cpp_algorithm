//
// Created by LiHeng on 2020/4/28.
//

// leetcode 17 电话按键
#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <typeinfo>

using namespace std ;

class Solution{
private:
    const string LetterMap[10] = {
            " " , "" , "abc" , "def" , "ghi" , "jkl" , "mno" , "pqrs" , "tuv" , "wxyz" } ;

    vector<string> res ;
    //digits是数字字符串，index是digits的索引， s存储的是转化digits[0...index-1]所获得的字母字符串
    void findCombination(const string& digits , int index ,  const string& s){

        if(index == digits.size()){
            res.push_back(s) ;
            return;
        }

        char c = digits[index] ;
        assert(c >= '0' && c <= '9' && c!='1') ;
        string letters = LetterMap[c - '0'] ;
        //int tem = c - '0' ;
        //cout << typeid(tem).name() <<endl ;
        //cout << c - '0' <<" :" << LetterMap[c - '0'] << endl ;

        for(int i = 0 ; i < letters.size() ; i++){  //循环里面有递归，注意理解过程
            //cout << "digits[" << index << "] = " << c << " , use " << letters[i] << endl ;
            findCombination(digits , index + 1 , s + letters[i]) ;
        }
        return;
    }

public:
    vector<string> letterCombinations(string digits){
        res.clear() ;
        if(digits == "")
            return res ;

        findCombination(digits , 0 , "") ;
        return res ;
    }


};