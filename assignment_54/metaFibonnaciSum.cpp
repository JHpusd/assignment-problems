# include <iostream>
# include <cassert>

int calcFibTerm(int n)
{
    int fib_zero = 0;
    int fib_one = 1;
    int sum = 0;
    if (n == 0){
        return fib_zero;
    }
    if (n == 1){
        return fib_one;
    }
    for (int i = 0; i < n-1; i++){
        sum = fib_one + fib_zero;
        fib_zero = fib_one;
        fib_one = sum;
    }
    return sum;
}

int metaFibonacciSum(int n)
{
    int Fibonnaci[(calcFibTerm(n) + 1)] = {};
    int Partial[(calcFibTerm(n) + 1)] = {};

    for (int i = 0; i <= calcFibTerm(n); i++){
        if (i == 0){
            Fibonnaci[i] = 0;
        }
        else if (i == 1){
            Fibonnaci[i] = 1;
        }
        else{
            Fibonnaci[i] = Fibonnaci[i-1] + Fibonnaci[i-2];
        }
    }

    return Fibonnaci;
}

int main()
{
    std::cout << "Testing...\n";;

    std::cout << metaFibonacciSum(6) << "\n";

    std::cout << "Success!";

    return 0;
}