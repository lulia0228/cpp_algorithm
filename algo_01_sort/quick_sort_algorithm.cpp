

#include <iostream>
#include <vector>
#include <ctime>
using namespace std ;

//0.快排---挖坑法
void quick_Sort1(vector<int> &nums , int left , int right){
    if(left >= right)
        return;

    /*//随机快排思路：随机选择数组中的一个数 index和数组最后一个数进行交换，然后用随机选择的数x来作为枢轴进行划分。
    //这样的话，就不能说会轻易的找到最差的情况了，因为每一次排序选择的枢轴都是随机的
    srand(time(0));
    int index = rand()%(right - left + 1);
    swap(nums[left] , nums[left+index]) ; //随机选取的临界值的索引是边界起始值+取值范围的随机索引  */

    int value = nums[left] ; //选第一个作为基准值
    int i = left ;
    int j = right;
    while(i < j){
        while(i<j && nums[j] >= value) { j-- ;} //i<j 必须要有 防止数组越界
        if(i<j){
            nums[i] = nums[j] ;
            i++ ;
        }
        while(i<j && nums[i] <= value) { i++ ;} //i<j 必须要有 防止数组越界
        if(i<j){
            nums[j] = nums[i] ;
            j-- ;
        }
    }
    nums[i] = value ;//nums[i]=value;//当游标指针i和j重叠时将基准填入坑
    quick_Sort1(nums , left , i - 1) ;
    quick_Sort1(nums , i + 1 , right);
}


//1.快排---左右指针法
void quick_Sort2(vector<int> & nums , int left , int right){
    if(left >= right)
        return;
    int value = nums[left] ; //选第一个作为基准值
    int i = left ;
    int j = right;

    while(i<j){
        while (i<j && nums[j] >= value)  //注意基准值选数组第一个元素，要先从后面往前面找；
            j--;
        while (i<j && nums[i] <= value ) //注意基准值选数组最后一个元素，要先从前面往后面找；
            i++;
        if(i<j)
            swap(nums[i],nums[j]);
        else
            swap(nums[left] , nums[i]);
    }

    /*while(i<j){
        while (i<j && nums[j] >= value)  //注意基准值选数组第一个元素，要先从后面往前面找；
            j--;
        while (i<j && nums[i] <= value ) //注意基准值选数组最后一个元素，要先从前面往后面找；
            i++;
        swap(nums[i],nums[j]);
    }
    swap(nums[left] , nums[i]);*/

    quick_Sort2(nums , left , i - 1);
    quick_Sort2(nums, i + 1 , right );

}



int main(){
    int a[] = {4,1,7,6,9,2,8,0,3,5};
    vector<int> vec1(a , a+10);
    quick_Sort1(vec1, 0 , 9);
    for(int i = 0 ; i < vec1.size(); i++)
        cout << vec1[i] << "\t";

    cout << endl ;

    int b[] = {9,8,10,4,7,2,5};
    vector<int> vec2(b , b+7);
    quick_Sort2(vec2, 0 , 6);
    for(int i = 0 ; i < vec2.size(); i++)
        cout << vec2[i] << "\t";

}


