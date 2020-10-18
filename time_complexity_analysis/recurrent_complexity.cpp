
//递归算法时间复杂度分析：  先看层数，然后把每层调用时间复杂度加起来

#include <iostream>
#include <cassert>
using  namespace std ;

int sum(int n){
    assert(n >= 0) ; //递归深度是n
    if (n == 0)
        return 0;
    return n + sum(n-1) ;
}

//时间复杂度是n * O(1) = O(n)

//求x的n次方
double pow(double x , int n){

    if(n == 0 )
        return 1.0 ;

    if(n > 0 ){
        double t = pow(x , n/2) ;
        if (n%2 != 0)   //n为奇数
            return x*t*t ;
        return t*t ;
    }
    else{
        double t = pow(x , -n/2) ;
        if (-n%2 != 0)   //n为奇数
            return 1.0/(x*t*t) ;
        return 1.0/(t*t) ;
    }

}

//时间复杂度是 log2(n) * O(1) = O(logn)


//求2的n次方
int f(int n){
    assert( n >= 0 );
    if(n == 0)
        return 1;
    return f(n-1) + f(n-1) ;
}

//时间复杂度是 每层相加 1+....+2^n   O(2^n)


int main(){
    double x1 = 2.0 ;
    int n = -4 ;
    double re = pow(x1 , n) ;
    cout << re << endl ;
    int re2 = f(n);
    cout << re2 ;
}



