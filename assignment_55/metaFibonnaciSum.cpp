# include <iostream>
# include <cassert>

int calcFibTerm(int index){
    int fib_zero = 0;
    int fib_one = 1;
    int sum = 0;

    if (index == 0){
        return fib_zero;
    }
    if (index == 1){
        return fib_one;
    }
    for (int i = 0; i < index-1; i++){
        sum = fib_one + fib_zero;
        fib_zero = fib_one;
        fib_one = sum;
    }
    return sum;
}

int metaFibonacciSum(int n)
{

    if (n==1){return 1;}
    if (n==0){return 0;}

    int terms[n+1];
    for (int i = 0; i <= n; i++){
        terms[i] = calcFibTerm(i);
    }
    
    int extendedTerms[terms[n]+1];
    for (int i = 0; i <= terms[n]; i++){
        extendedTerms[i] = calcFibTerm(i);
    }

    int partialSums[terms[n]+1];
    int partSum = 0;
    for (int i = 0; i <= terms[n]; i++){
        partSum += extendedTerms[i];
        partialSums[i] = partSum;
    }
    
    int metaSum = 0;
    for (int i = 0; i <= n; i++){
        metaSum += partialSums[terms[i]];
    }
    return metaSum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!";

    return 0;
}