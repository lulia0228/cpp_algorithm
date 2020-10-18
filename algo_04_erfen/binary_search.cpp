
//二分查找针对的是有序数组
/*
#include <iostream>
int binarySearch(int arr[], int l, int r, int target){
//    if (l > r)
//        return -1;
    int mid = l + (r-l)/2; //可防止溢出，不采用（l+r）/2
//    std::cout << mid << std::endl;
    if (arr[mid] == target)
        return arr[mid];
    else if (arr[mid] > target)
        return binarySearch(arr, l, mid-1, target);
    else
        return binarySearch(arr, mid+1, r, target);
}

int main(){
    int array[] = {1,2,3,4,5,6}; //用花括号
    int result = binarySearch(array, 0, 5, 5);
    std::cout << result;
}
*/

//更通用的模板写法
#include <iostream>
#include <cmath>
#include <cassert>
#include <ctime>

using namespace std;

template <typename T>
int binarySearch(T arr[], int n, T target){
    int l = 0, r = n-1;
    while(l <= r){
      int mid = l + (r-l)/2;
      if (arr[mid] == target)
          return mid;
      if (arr[mid] > target)
          r = mid - 1;
      else
          l = mid + 1;
    }
    return -1;
}

int* generateOrderedArray(int n){
    assert(n > 0);
    int* arr = new int[n];
    for (int i = 0;i < n; i++)
        arr[i] = i;
    return arr;
}

int main(){
    int n = 10000000;
    int* data = generateOrderedArray(n);
    clock_t startTime = clock();
    for (int i = 0; i < n; i++)
        assert(i == binarySearch(data, n, i));
    clock_t endTime = clock();
    //delete data ;
    cout << "binarySearch test complete."<< endl;
    cout << "Time cost:"<< double(endTime-startTime)/CLOCKS_PER_SEC<<" s"<<endl;
    return 0;
}




