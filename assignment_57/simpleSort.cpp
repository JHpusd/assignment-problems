# include <iostream>
# include <cassert>
int main()
{
    int arr[5]{ 30, 50, 20, 10, 40 };

    int counter = 0;
    int len = sizeof(arr)/sizeof(arr[0]);

    for (int n = 0; n <= (len-1); n++){
        int smallestVal = arr[counter];
        int smallestIndex = counter;
        for (int i = counter; i <= (len-1); i++){
            if (arr[i] < smallestVal){
                smallestIndex = i;
                smallestVal = arr[i];
            }
        }
        arr[smallestIndex] = arr[counter];
        arr[counter] = smallestVal;
        counter += 1;
    }

    std::cout << "Testing...\n";

    assert(arr[0]==10);
    assert(arr[1]==20);
    assert(arr[2]==30);
    assert(arr[3]==40);
    assert(arr[4]==50);

    std::cout << "Succeeded";

    return 0;
}