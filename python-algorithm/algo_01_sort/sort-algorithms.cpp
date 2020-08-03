//
// Created by LiHeng on 2019/8/25.
//

#include <iostream>
using namespace std ;

//冒泡排序:相邻元素交换，每一轮让最值靠近边缘
int* bubbleSort(int* arry , int n){
    for(int i = 0 ; i < n ; i++){
        // 没有数据交换,提前退出冒泡循环的标志位
        bool flag = false ;
        //一轮交换后最大值会转移到最末尾
        for(int j = 0 ; j < n-i-1 ; j++){
            if(arry[j] > arry[j+1]){
                swap(arry[j] , arry[j+1]);
                flag = true ;
            }
        }
        if(!flag)
            break;
    }
    return arry ;
}

//插入排序: 选择未排序区间的首元素和已排序区间的每个元素作比较确定插入位置，同时插入位置以后的元素索引都要加1
int* insertionSort(int* arry , int n){
    for(int i = 1 ; i < n ; i++){
        int value = arry[i];
        int j = i-1 ;

        for(; j >= 0 ; j--)
            if ( value <  arry[j] ) //从大到小 只需要变成大于号
                arry[j+1] = arry[j] ;
            else
                break ; //else 这句不能落下，否则j的下标会一直更新

        arry[j+1] = value ;
    }
    return arry ;
}

//选择排序：1.从未排序区间找到最小值 2.和已排序区间后面一个值交换
int* selectionSort(int* arry , int n){
    for(int i = 0 ; i < n ; i++){
        int minIndex = i;
        for(int j = i+1 ; j<n ; j++)
            if (arry[j] < arry[minIndex]) // 从大到小 只需要变成大于号
                minIndex = j;
        swap(arry[i] , arry[minIndex]);
    }
    return arry ;
}


int main(){
    int arry[7]  = {3,1,5,2,4,8,7};

    int* p0  = bubbleSort(arry , 7 );
    for(int i = 0 ; i < 7 ; i++){
        cout << *p0 <<"\t";
        p0++ ;
    }
    cout <<endl ;
    int* p1  = insertionSort(arry , 7 );
    for(int i = 0 ; i < 7 ; i++){
        cout << *p1 <<"\t";
        p1++ ;
    }
    cout <<endl ;
    int* p2  = selectionSort(arry , 7 );
    for(int i = 0 ; i < 7 ; i++){
        cout << *p2 <<"\t";
        p2++ ;
    }
    return 0 ;
}

