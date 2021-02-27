#include <iostream>
#include <cassert>

int calcIndex(int num){
    int index = 0;
    int fib1 = 0;
    int fib2 = 1;

    while (true){
        if (fib2 > num){
            return index + 1;
        }
        int sum = fib1 + fib2;
        fib1 = fib2;
        fib2 = sum;
        index += 1;
    }
}

int main() {
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}