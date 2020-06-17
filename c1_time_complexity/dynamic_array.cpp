//
// Created by liheng on 19-8-6.
//

//分析均摊时间复杂度

#include <iostream>
#include <cassert>
#include <ctime>
#include <cmath>

using namespace std;

template  <typename T>
class MyVector{
private:
    T* data ;
    int capacity ;
    int size ;

    void resize( int newCapacity){
        assert(newCapacity >= size) ;
        T* newData = new T[newCapacity] ;
        for(int i = 0; i< size ; i++)
            newData[i] = data[i] ;
        delete[] data;
        data = newData ;
        capacity = newCapacity;
    }

public:
    MyVector(){
        data = new T[10];
        capacity =10 ;
        size = 0;
    }

    ~MyVector(){
        delete[] data ;
    }

    void push_back(T e){
        //assert(size < capacity) ;
        if(size == capacity)
            resize( 2*capacity);
        data[size++] = e ;
    }

    T pop_back(){
        assert( size > 0);
        T ret = data[size-1] ; //防止下面if(size == capacity/2)时候 data[size-1]数据被抹掉.
        size-- ;
        // if(size == capacity/2)
        if(size == capacity/4) //除以4防止均摊复杂度震荡
            resize(capacity/2);
        return ret ;
    }
};


int main(){
    for(int i = 10 ; i <= 26 ; i++){
        int n = pow(2, i) ;
        clock_t startTime = clock();
        MyVector<int> vec ;
        for (int i = 0 ; i < n ; i++)
            vec.push_back(i);
        for (int i = 0 ; i < n ; i++)
            vec.pop_back();
        clock_t endTime = clock();
        cout << 2*n << " operations: \t" ;
        cout << double(endTime-startTime)/CLOCKS_PER_SEC << " s" << endl;
    }
    return 0 ;
}

