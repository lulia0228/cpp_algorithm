//
// Created by LiHeng on 2019/7/28.
//

//复杂度实验
#include <iostream>
#include <cassert>
#include <ctime>
#include <cmath>
#include <MyAlgorithmTester.h>
#include <MyUtil.h>

using namespace std ;
//using namespace MyUtil ;
//using namespace MyAlgorithmTester;

//每次让数据量扩大2倍进行测试
int main(){

    // 验证O(n)时间复杂度
    cout << "Test O(n) : " << endl ;
    for(int i = 20; i <= 27 ;i++){
        int n = pow(2, i);
        int* arr = MyUtil::generateRandomArray(n , 0 ,10e8) ;
        clock_t startTime = clock();
        MyAlgorithmTester::findMax(arr , n);
        clock_t endTime = clock();
        cout << "data size 2^" << i << "=" << n << "\t";
        cout << "Time cost: " << double(endTime - startTime)/CLOCKS_PER_SEC << endl;
        delete[] arr ;
    }

    // 验证O(n^2)时间复杂度
    cout << "Test O(n^2) : " << endl ;
    for(int i = 10; i <= 15 ;i++){
        int n = pow(2, i);
        int* arr = MyUtil::generateRandomArray(n , 0 ,10e8) ;
        clock_t startTime = clock();
        MyAlgorithmTester::selectionSort(arr , n);
        clock_t endTime = clock();
        cout << "data size 2^" << i << "=" << n << "\t";
        cout << "Time cost: " << double(endTime - startTime)/CLOCKS_PER_SEC << endl;
        delete[] arr ;
    }


    // 验证O(nlogn)时间复杂度
    cout << "Test O(nlogn) : " << endl ;
    for(int i = 20; i <= 26 ;i++){
        int n = pow(2, i);
        int* arr = MyUtil::generateRandomArray(n , 0 ,1<<30) ;
        clock_t startTime = clock();
        MyAlgorithmTester::mergeSort(arr , n);
        clock_t endTime = clock();
        cout << "data size 2^" << i << "=" << n << "\t";
        cout << "Time cost: " << double(endTime - startTime)/CLOCKS_PER_SEC << endl;
        delete[] arr ;
    }

    // 验证O(logn)时间复杂度  二分查找用于顺序数组  1秒内可处理的数据比较大，这里由于内存分配问题，无法测试出来;
    // 极限2的31次方 减去1 不要乱搞 小心搞坏硬件
    cout << "Test O(logn) : " << endl ;
    for(int i = 20; i <= 30 ; i++){
        int n = pow(2, i);
        int* arr = MyUtil::generateOrderedArray(n-2) ;
        clock_t startTime = clock();
        MyAlgorithmTester::binarySearch(arr , n  , 0);
        clock_t endTime = clock();
        cout << "data size 2^" << i << "=" << n << "\t";
        cout << "Time cost: " << double(endTime - startTime)/CLOCKS_PER_SEC << endl;
        delete[] arr ;
    }

    return 0 ;
}

