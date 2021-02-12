# include <iostream>
# include <cassert>

int seqSum(int n){
    if (n==0){
        return 0;
    }
    int seqList[n+1];
    int sum = 1;

    seqList[0] = 0;
    seqList[1] = 1;
    for (int i = 2; i <= n; i++){
        seqList[i] = seqList[i-1] + 2*seqList[i-2];
        sum += seqList[i];
    }
    return sum;
}

int extendedSeqSum(int n){
    int seqList[n+1];
    int extendedSum = 1;

    seqList[0] = 0;
    seqList[1] = 1;
    for (int i = 2; i <= n; i++){
        seqList[i] = seqList[i-1] + 2*seqList[i-2];
    }

    int extendedSeqList[seqList[n]+1];
    extendedSeqList[0] = 0;
    extendedSeqList[1] = 1;
    for (int i = 2; i<=seqList[n]; i++){
        extendedSeqList[i] = extendedSeqList[i-1] + 2*extendedSeqList[i-2];
        extendedSum += extendedSeqList[i];
    }
    return extendedSum;
}

// write your functions seqSum and extendedSeqSum here

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}